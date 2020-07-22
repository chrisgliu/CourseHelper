"use strict";
// --- making a request for data ---
function requestAJAX(url_source, workspace_id, add_data_function) {
    let my_request = new XMLHttpRequest();
    my_request.open('GET', url_source, true);
    my_request.onload = () => {
        if (my_request.status == 200) {
            let response = my_request.responseXML;
            if (response != null) {
                add_data_function(workspace_id, response);
            }
        }
    };
    my_request.send();
    // cant return value in an asynchronous request
}
// --- spaces in url_source ---
function substituteChar(message, spot, item) {
    let before = message.substring(0, spot);
    let after = message.substring(spot + 1);
    let result = before + item + after;
    return result;
}
function substituteURLSpace(message) {
    let edited_message = message;
    if (message.indexOf(' ') == -1) {
        return message;
    }
    for (let index = 0; index < message.length; index++) {
        let char = message.charAt(index);
        if (char == ' ') {
            edited_message = substituteChar(edited_message, index, '%20');
        }
    }
    return edited_message;
}
function showIt(id) {
    let element = document.getElementById(id);
    if (element == null) {
        return;
    }
    element.style.display = 'block';
}
function dontShowIt(id) {
    let element = document.getElementById(id);
    if (element == null) {
        return;
    }
    element.style.display = 'none';
}
function toggleIt(element) {
    if (element == null) {
        return;
    }
    if (element.style.display === 'block') {
        element.style.display = 'none';
    }
    else {
        element.style.display = 'block';
    }
}
function toggleShow(id) {
    let element = document.getElementById(id);
    toggleIt(element);
}
/// <reference path='toggle.ts'/>
function clearData(ul_id) {
    let list = document.getElementById(ul_id);
    if (list == null) {
        return;
    }
    while (list.firstChild) {
        let child = list.lastChild;
        if (child != null) {
            list.removeChild((child));
        }
    }
}
function addDataList(parent_ul_id, name) {
    let parent = document.getElementById(parent_ul_id);
    if (parent == null) {
        return;
    }
    let toggle = document.createElement('li');
    let symbol = document.createElement('span');
    symbol.innerHTML = name;
    symbol.className = 'caret';
    symbol.onclick = () => {
        let data = symbol.parentElement.querySelector(".nested");
        toggleIt(data);
        symbol.classList.toggle("caret-down");
    };
    let nested = document.createElement('ul');
    nested.className = 'nested';
    nested.id = name;
    toggle.appendChild(symbol);
    toggle.appendChild(nested);
    parent.appendChild(toggle);
}
function addSpecificData(ul_id, info) {
    let list = document.getElementById(ul_id);
    if (list == null) {
        return;
    }
    let data = document.createElement('li');
    data.innerHTML = info;
    list.appendChild(data);
}
function getSubListNames(parent_ul_id) {
    let names = [];
    let parent = document.getElementById(parent_ul_id);
    if (parent == null) {
        return;
    }
    let data = parent.children;
    for (let index = 0; index < data.length; index++) {
        let listitem = data[index];
        let name = listitem.getElementsByTagName('span')[0].innerHTML;
        names.push(name);
    }
    return names;
}
function addSessionDataList(data, data_name) {
    for (let index = 0; index < data.length; index++) {
        let value = data[index];
        let key = data_name + "-" + index;
        window.sessionStorage.setItem(key, value);
    }
}
function addSessionCourses(majors, categories, subcategories, requirements, courses, prereqs, ap) {
    addSessionDataList(majors, "major");
    addSessionDataList(categories, "category");
    addSessionDataList(subcategories, "subcategory");
    addSessionDataList(requirements, "requirement");
    addSessionDataList(courses, "course");
    addSessionDataList(prereqs, "prereq");
    addSessionDataList(ap, "test");
}
function clearSession() {
    window.sessionStorage.clear();
}
function removeSessionData(data_id) {
    window.sessionStorage.removeItem(data_id);
}
function getSessionData(data_id) {
    let data = window.sessionStorage.getItem(data_id);
    return data;
}
///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
///<reference path='sessiondata.ts'/>
// courses tree data
function readMajors(majors) {
    let major_data = [];
    for (const major of majors) {
        let major_content = major.childNodes;
        let major_name = '';
        let categories_node = null;
        for (const node of major_content) {
            if (node.nodeName == 'major_name') {
                major_name = node.textContent;
            }
            if (node.nodeName == 'categories' && node.hasChildNodes()) {
                categories_node = node;
            }
        }
        let data = { 'major_name': major_name, 'categories': categories_node };
        major_data.push(data);
    }
    return major_data;
}
function readCategories(categories) {
    let category_data = [];
    for (const category of categories) {
        let category_content = category.childNodes;
        let category_name = '';
        let subcategories_node = null;
        for (const node of category_content) {
            if (node.nodeName == 'category_name') {
                category_name = node.textContent;
            }
            if (node.nodeName == 'subcategories' && node.hasChildNodes()) {
                subcategories_node = node;
            }
        }
        let data = { 'category_name': category_name, 'subcategories': subcategories_node };
        category_data.push(data);
    }
    return category_data;
}
function readSubcategories(subcategories) {
    let subcategory_data = [];
    for (const subcategory of subcategories) {
        let subcategory_content = subcategory.childNodes;
        let subcategory_name = '';
        let requirements_node = null;
        for (const node of subcategory_content) {
            if (node.nodeName == 'subcategory_name') {
                subcategory_name = node.textContent;
            }
            if (node.nodeName == 'requirements' && node.hasChildNodes()) {
                requirements_node = node;
            }
        }
        let data = { 'subcategory_name': subcategory_name, 'requirements': requirements_node };
        subcategory_data.push(data);
    }
    return subcategory_data;
}
function readRequirements(requirements) {
    let requirement_data = [];
    for (const requirement of requirements) {
        let requirement_content = requirement.childNodes;
        let requirement_name = '';
        let courses_node = null;
        for (const node of requirement_content) {
            if (node.nodeName == 'requirement_name') {
                requirement_name = node.textContent;
            }
            if (node.nodeName == 'courses' && node.hasChildNodes()) {
                courses_node = node;
            }
        }
        let data = { 'requirement_name': requirement_name, 'courses': courses_node };
        requirement_data.push(data);
    }
    return requirement_data;
}
function readCourses(courses) {
    let course_data = [];
    for (const course of courses) {
        let course_content = course.childNodes;
        let course_name = '';
        let prereqs_node = null;
        let ap_node = null;
        for (const node of course_content) {
            if (node.nodeName == 'course_name') {
                course_name = node.textContent;
            }
            if (node.nodeName == 'prereqs' && node.hasChildNodes()) {
                prereqs_node = node;
            }
            if (node.nodeName == 'ap' && node.hasChildNodes()) {
                ap_node = node;
            }
        }
        let data = { 'course_name': course_name, 'prereqs': prereqs_node, 'ap': ap_node };
        course_data.push(data);
    }
    return course_data;
}
function readPrereqs(prereqs) {
    let prereq_data = [];
    for (const prereq of prereqs) {
        let prereq_content = prereq.childNodes;
        let prereq_name = '';
        for (const node of prereq_content) {
            if (node.nodeName == 'prereq_name') {
                prereq_name = node.textContent;
            }
        }
        prereq_data.push(prereq_name);
    }
    return prereq_data;
}
function readAp(ap) {
    let ap_data = [];
    for (const ap_test of ap) {
        let test_content = ap_test.childNodes;
        let test_name = '';
        for (const node of test_content) {
            if (node.nodeName == 'test_name') {
                test_name = node.textContent;
            }
        }
        ap_data.push(test_name);
    }
    return ap_data;
}
function addCoursesData(workspace_id, response) {
    // -- data tree --
    // ex major:major_name
    // -- session catalog ---
    let session_majors = []; //ex  major
    let session_categories = []; //ex major/category
    let session_subcategories = []; //ex major/category/subcategory
    let session_requirements = []; //ex major/category/subcategory/requirement
    let session_courses = []; //ex major/category/subcategory/requirement/course
    let session_prereqs = []; //ex  major/category/subcategory/requirement/course/prereq/course
    let session_ap = []; //ex  major/category/subcategory/requirement/course/test/testname
    // ---
    let majors = response.getElementsByTagName('major');
    let major_data = readMajors(majors);
    for (const major of major_data) {
        // data tree
        addDataList(workspace_id, `Major:${major.major_name}`);
        // session
        session_majors.push(major.major_name);
        if (major.categories != null) {
            let categories = major.categories.childNodes;
            let category_data = readCategories(categories);
            for (const category of category_data) {
                // data tree
                addDataList(`Major:${major.major_name}`, `Category:${category.category_name}`);
                // session
                session_categories.push(`${major.major_name}/${category.category_name}`);
                if (category.subcategories != null) {
                    let subcategories = category.subcategories.childNodes;
                    let subcategory_data = readSubcategories(subcategories);
                    for (const subcategory of subcategory_data) {
                        // data tree
                        addDataList(`Category:${category.category_name}`, `Subcategory:${subcategory.subcategory_name}`);
                        // session
                        session_subcategories.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}`);
                        if (subcategory.requirements != null) {
                            let requirements = subcategory.requirements.childNodes;
                            let requirement_data = readRequirements(requirements);
                            for (const requirement of requirement_data) {
                                // data tree
                                addDataList(`Subcategory:${subcategory.subcategory_name}`, `Requirement:${requirement.requirement_name}`);
                                // session
                                session_requirements.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}`);
                                if (requirement.courses != null) {
                                    let courses = requirement.courses.childNodes;
                                    let course_data = readCourses(courses);
                                    for (const course of course_data) {
                                        // data tree
                                        addDataList(`Requirement:${requirement.requirement_name}`, `Course:${course.course_name}`);
                                        // session
                                        session_courses.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}`);
                                        if (course.prereqs != null) {
                                            // data tree
                                            addDataList(`Course:${course.course_name}`, `Prereq:${course.course_name}`);
                                            let prereqs = course.prereqs.childNodes;
                                            let prereq_data = readPrereqs(prereqs);
                                            for (const prereq of prereq_data) {
                                                addSpecificData(`Prereq:${course.course_name}`, prereq);
                                                // session
                                                session_prereqs.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/prereq/${prereq}`);
                                            }
                                        }
                                        if (course.ap != null) {
                                            // data tree
                                            addDataList(`Course:${course.course_name}`, `Ap:${course.course_name}`);
                                            let ap = course.ap.childNodes;
                                            let ap_data = readAp(ap);
                                            for (const ap_test of ap_data) {
                                                addSpecificData(`Ap:${course.course_name}`, ap_test);
                                                // session
                                                session_ap.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/test/${ap_test}`);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    addSessionCourses(session_majors, session_categories, session_subcategories, session_requirements, session_courses, session_prereqs, session_ap);
}
function updateCoursesData() {
    let workspace_id = 'coursesdata';
    clearData(workspace_id);
    let url_source = '/requestcoursesdata';
    requestAJAX(url_source, workspace_id, addCoursesData);
}
function activateCourseButtons() {
    let forms = ['majorforms', 'categoryforms', 'subcategoryforms',
        'requirementforms', 'courseforms', 'prereqforms', 'apforms'];
    let refresh = document.getElementById('refreshcoursesdata');
    // refresh button is shown only when user is signed in
    if (refresh != null) {
        refresh.onclick = () => { updateCoursesData(); };
        document.getElementById('majoroperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('majorforms');
        };
        document.getElementById('categoryoperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('categoryforms');
        };
        document.getElementById('subcategoryoperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('subcategoryforms');
        };
        document.getElementById('requirementoperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('requirementforms');
        };
        document.getElementById('courseoperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('courseforms');
        };
        document.getElementById('prereqoperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('prereqforms');
        };
        document.getElementById('apoperation').onclick = () => {
            for (const item of forms) {
                dontShowIt(item);
            }
            showIt('apforms');
        };
    }
}
///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
//helperdata
function activateHelperButtons() {
    let actions = ['mymajoractions', 'mytermactions', 'myapactions',
        'tranfercredit', 'status',
        'mycourseoperation'];
    document.getElementById('mymajorbutton').onclick = () => {
        for (const item of actions) {
            dontShowIt(item);
        }
        showIt('mymajoractions');
    };
    //testing
    document.getElementById('testbuttonterm').onclick = () => {
        for (const item of actions) {
            dontShowIt(item);
        }
        showIt('mytermactions');
    };
    document.getElementById('testbuttonap').onclick = () => {
        for (const item of actions) {
            dontShowIt(item);
        }
        showIt('myapactions');
    };
    document.getElementById('testbuttontranfer').onclick = () => {
        for (const item of actions) {
            dontShowIt(item);
        }
        showIt('tranfercredit');
    };
    document.getElementById('testbuttonstatus').onclick = () => {
        for (const item of actions) {
            dontShowIt(item);
        }
        showIt('status');
    };
    ///testing
    document.getElementById('mycoursesbutton').onclick = () => {
        showIt('mycourseoperation');
    };
    document.getElementById('myapbutton').onclick = () => {
        showIt('mytestoperation');
    };
}
/// <reference path='toggle.ts'/>
/// <reference path="coursesdata.ts" />
/// <reference path="helperdata.ts" />
document.addEventListener("DOMContentLoaded", () => {
    // nav buttons
    document.getElementById('creditsneeded').onclick = () => {
        showIt('section-b');
        dontShowIt('section-a');
        dontShowIt('section-c');
    };
    document.getElementById('creditswanted').onclick = () => {
        showIt('section-c');
        dontShowIt('section-a');
        dontShowIt('section-b');
    };
    let signin = document.getElementById('signin');
    if (signin != null) {
        signin.onclick = () => { showIt('signinform'); };
    }
    let signup = document.getElementById('signup');
    if (signup != null) {
        signup.onclick = () => { showIt('signupform'); };
    }
    let signout = document.getElementById('signout');
    if (signout != null) {
        signout.onclick = () => { window.location.href = '/signOut'; };
    }
    document.getElementById('cancelsignin').onclick = () => {
        dontShowIt('signinform');
    };
    document.getElementById('cancelsignup').onclick = () => {
        dontShowIt('signupform');
    };
    // course buttons
    activateCourseButtons();
    // helper buttons
    activateHelperButtons();
});
