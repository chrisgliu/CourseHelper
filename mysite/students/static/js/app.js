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
function addSpecificData(ul_id, info) {
    let list = document.getElementById(ul_id);
    if (list == null) {
        return;
    }
    let data = document.createElement('li');
    data.innerHTML = info;
    list.appendChild(data);
}
function addDataList(parent_ul_id, name, symbol_type, toggle_function) {
    let parent = document.getElementById(parent_ul_id);
    if (parent == null) {
        return;
    }
    let toggle = document.createElement('li');
    let symbol = document.createElement('span');
    symbol.innerHTML = name;
    symbol.className = symbol_type;
    symbol.onclick = () => {
        toggle_function(symbol);
    };
    let nested = document.createElement('ul');
    nested.className = 'nested';
    nested.id = name;
    toggle.appendChild(symbol);
    toggle.appendChild(nested);
    parent.appendChild(toggle);
}
let special_actions = ['mymajoractions', 'mytermactions', 'myapactions',
    'tranfercredit', 'status',
    'mycourseoperation'];
function addCaretList(parent_ul_id, name, is_special, special_id) {
    let toggle_function = function click(symbol) {
        let data = symbol.parentElement.querySelector(".nested");
        toggleIt(data);
        symbol.classList.toggle("caret-down");
        if (is_special) {
            let element = document.getElementById(special_id);
            for (const item of special_actions) {
                dontShowIt(item);
            }
            toggleIt(element);
        }
    };
    addDataList(parent_ul_id, name, 'caret', toggle_function);
}
function addStatusList(parent_ul_id, name, status) {
    let mark = 'xmark';
    if (status) {
        mark = 'checkmark';
    }
    let toggle_function = function click(symbol) {
        let data = symbol.parentElement.querySelector(".nested");
        toggleIt(data);
        if (status) {
            symbol.classList.toggle("checkmark_down");
        }
        else {
            symbol.classList.toggle("xmark-down");
        }
    };
    addDataList(parent_ul_id, name, mark, toggle_function);
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
function addSessionDataList(data, data_name) {
    for (let index = 0; index < data.length; index++) {
        let value = data[index];
        let key = data_name + "-" + index;
        window.sessionStorage.setItem(key, value);
    }
}
function clearSessionDataList(data_name) {
    let index = 0;
    let key = data_name + "-" + index;
    let data = window.sessionStorage.getItem(key);
    while (data != null) {
        window.sessionStorage.removeItem(key);
        index += 1;
        key = data_name + "-" + index;
        data = window.sessionStorage.getItem(key);
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
function addSessionMajors(majors) {
    addSessionDataList(majors, "mymajor");
}
function addSessionAP(ap) {
    addSessionDataList(ap, "myap");
}
function addSessionPlanner(years, semesters) {
    addSessionDataList(years, "myyear");
    addSessionDataList(semesters, "mysemester");
}
function addSessionSchedule(schedules, courses) {
    addSessionDataList(schedules, "myschedule");
    addSessionDataList(courses, "mycourse");
}
function readXMLNodes(tags, subdatatags, subparenttags) {
    let tag_data = [];
    for (const tag of tags) {
        let tag_content = tag.childNodes;
        let subtag_data = {};
        for (const node of tag_content) {
            for (const subtag of subdatatags) {
                if (node.nodeName == subtag) {
                    subtag_data[subtag] = node.textContent;
                }
            }
            if (subparenttags != null) {
                for (const subtag of subparenttags) {
                    if (node.nodeName == subtag) {
                        subtag_data[subtag] = node;
                    }
                }
            }
        }
        tag_data.push(subtag_data);
    }
    return tag_data;
}
function readMainTags(tags, subdatatags, subparenttags) {
    return readXMLNodes(tags, subdatatags, subparenttags);
}
function readSubNodeList(list, subdatatags, subparenttags) {
    return readXMLNodes(list, subdatatags, subparenttags);
}
///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
///<reference path='sessiondata.ts'/>
/// <reference path="readXML.ts" />
// courses tree data
// --- courses data helper functions ---
function readMajors(majors) {
    return readMainTags(majors, ["major_name",], ["categories",]);
}
function readCategories(categories) {
    return readSubNodeList(categories, ["category_name",], ["subcategories",]);
}
function readSubcategories(subcategories) {
    return readSubNodeList(subcategories, ["subcategory_name",], ["requirements",]);
}
function readRequirements(requirements) {
    return readSubNodeList(requirements, ["requirement_name",], ["courses",]);
}
function readCourses(courses) {
    return readSubNodeList(courses, ["course_name",], ["prereqs", "ap"]);
}
function readPrereqs(prereqs) {
    return readSubNodeList(prereqs, ["prereq_name",], null);
}
function readAp(ap) {
    return readSubNodeList(ap, ["test_name",], null);
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
        addCaretList(workspace_id, `Major:${major.major_name}`, false, null);
        // session
        session_majors.push(major.major_name);
        if (major.categories != null) {
            let categories = major.categories.childNodes;
            let category_data = readCategories(categories);
            for (const category of category_data) {
                // data tree
                addCaretList(`Major:${major.major_name}`, `Category:${category.category_name}`, false, null);
                // session
                session_categories.push(`${major.major_name}/${category.category_name}`);
                if (category.subcategories != null) {
                    let subcategories = category.subcategories.childNodes;
                    let subcategory_data = readSubcategories(subcategories);
                    for (const subcategory of subcategory_data) {
                        // data tree
                        addCaretList(`Category:${category.category_name}`, `Subcategory:${subcategory.subcategory_name}`, false, null);
                        // session
                        session_subcategories.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}`);
                        if (subcategory.requirements != null) {
                            let requirements = subcategory.requirements.childNodes;
                            let requirement_data = readRequirements(requirements);
                            for (const requirement of requirement_data) {
                                // data tree
                                addCaretList(`Subcategory:${subcategory.subcategory_name}`, `Requirement:${requirement.requirement_name}`, false, null);
                                // session
                                session_requirements.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}`);
                                if (requirement.courses != null) {
                                    let courses = requirement.courses.childNodes;
                                    let course_data = readCourses(courses);
                                    for (const course of course_data) {
                                        // data tree
                                        addCaretList(`Requirement:${requirement.requirement_name}`, `Course:${course.course_name}`, false, null);
                                        // session
                                        session_courses.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}`);
                                        if (course.prereqs != null) {
                                            // data tree
                                            addCaretList(`Course:${course.course_name}`, `Prereq:${course.course_name}`, false, null);
                                            let prereqs = course.prereqs.childNodes;
                                            let prereq_data = readPrereqs(prereqs);
                                            for (const prereq of prereq_data) {
                                                addSpecificData(`Prereq:${course.course_name}`, prereq.prereq_name);
                                                // session
                                                session_prereqs.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/prereq/${prereq.prereq_name}`);
                                            }
                                        }
                                        if (course.ap != null) {
                                            // data tree
                                            addCaretList(`Course:${course.course_name}`, `Ap:${course.course_name}`, false, null);
                                            let ap = course.ap.childNodes;
                                            let ap_data = readAp(ap);
                                            for (const ap_test of ap_data) {
                                                addSpecificData(`Ap:${course.course_name}`, ap_test.test_name);
                                                // session
                                                session_ap.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/test/${ap_test.test_name}`);
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
// resulting ajax function
function updateCoursesData() {
    let workspace_id = 'coursesdata';
    clearData(workspace_id);
    let url_source = '/requestcoursesdata';
    requestAJAX(url_source, workspace_id, addCoursesData);
}
///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
/// <reference path='sessiondata.ts' />
/// <reference path='readXML.ts' />
//helperdata
// my majors
// --- major helper functions ---
function addListedMajors(workspace_id, response) {
    let session_mymajors = [];
    let majors = response.getElementsByTagName('major');
    for (const major of majors) {
        session_mymajors.push(major.innerHTML);
    }
    //display majors in tracker
    //add session data
    addSessionMajors(session_mymajors);
}
// ---
// resulting ajax function
function updateMajorData() {
    let workspace_id = 'majorstracked';
    clearData(workspace_id);
    let url_source = '/requestmymajors';
    requestAJAX(url_source, workspace_id, addListedMajors);
}
// my ap
// --- ap helper functions ---
function readMyAP(tests) {
    return readMainTags(tests, ["test_name", "test_score"], null);
}
function addListedAp(workspace_id, response) {
    let session_myap = [];
    let tests = response.getElementsByTagName('test');
    let test_data = readMyAP(tests);
    for (const test of test_data) {
        let info = `${test.test_name}/${test.test_score}`;
        session_myap.push(info);
    }
    //display majors in tracker
    //add session data
    addSessionAP(session_myap);
}
// ---
// resulting ajax function
function updateAPData() {
    let workspace_id = '';
    clearData(workspace_id);
    let url_source = '/requestmytransfercredit';
    requestAJAX(url_source, workspace_id, addListedAp);
}
// my planner
// --- planner helper functions ---
function readMyYears(years) {
    return readMainTags(years, ["year_name",], ["semesters",]);
}
function readMySemesters(semesters) {
    return readSubNodeList(semesters, ["semester_name",], null);
}
function addPlannerData(workspace_id, response) {
    // --- session catalog ---
    let session_years = []; // ex year
    let session_semesters = []; // ex year/semester
    // ---
    let years = response.getElementsByTagName('year');
    let year_data = readMyYears(years);
    for (const year of year_data) {
        // data tree
        if (year.year_name == "before") {
            addCaretList(workspace_id, `Year:${year.year_name}`, true, "myapactions");
        }
        else {
            // addCaretList(workspace_id, `Year:${year.year_name}`, false, null);
            addStatusList(workspace_id, `Year:${year.year_name}`, true);
        }
        // session
        session_years.push(year.year_name);
        if (year.semesters != null) {
            let semesters = year.semesters.childNodes;
            let semester_data = readMySemesters(semesters);
            for (const semester of semester_data) {
                // data tree
                addCaretList(`Year:${year.year_name}`, semester.semester_name, true, "mytermactions");
                // session
                session_semesters.push(`${year.year_name}/${semester.semester_name}`);
            }
        }
    }
    addSessionPlanner(session_years, session_semesters);
}
// resulting ajax function
function updatePlannerData() {
    let workspace_id = 'plannerdata';
    clearData(workspace_id);
    let url_source = '/requestmyplanner';
    requestAJAX(url_source, workspace_id, addPlannerData);
}
// my schedule
// --- schedule helper functions ---
function readMySchedules(schedules) {
    return readMainTags(schedules, ["schedule_name",], ["courses",]);
}
function readMyCourses(courses) {
    return readSubNodeList(courses, ["course_name",], null);
}
function addScheduleData(workspace_id, response) {
    // --- session catalog ---
    let session_schedules = []; // ex sched (semester)
    let session_courses = []; // ex sched/course
    // ---
    let schedules = response.getElementsByTagName('schedule');
    let schedule_data = readMySchedules(schedules);
    for (const schedule of schedule_data) {
        // session
        session_schedules.push(schedule.schedule_name);
        let courses = schedule.courses.childNodes;
        let course_data = readMyCourses(courses);
        for (const course of course_data) {
            // session
            session_courses.push(`${schedule.schedule_name}/${course.course_name}`);
        }
    }
    addSessionSchedule(session_schedules, session_courses);
}
// resulting ajax function
function updateScheduleData() {
    let workspace_id = '';
    clearData(workspace_id);
    let url_source = '/requestmyschedule';
    requestAJAX(url_source, workspace_id, addScheduleData);
}
/// <reference path='toggle.ts'/>
/// <reference path="coursesdata.ts" />
/// <reference path="helperdata.ts" />
//some button functions for toggling
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
function activateHelperButtons() {
    let actions = ['mymajoractions', 'mytermactions', 'myapactions',
        'tranfercredit', 'status',
        'mycourseoperation'];
    let update = document.getElementById('updatehelperdata');
    // update button is shown only when user is signed in
    if (update != null) {
        update.onclick = () => {
            updateMajorData();
            updateAPData();
            updatePlannerData();
            updateScheduleData();
        };
    }
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
/// <reference path="buttons.ts" />
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
