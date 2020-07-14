"use strict";
// --- making a request for data ---
function requestAJAX(url_source, workspace_id, add_data_function) {
    let my_request = new XMLHttpRequest();
    my_request.open('GET', url_source, true);
    my_request.onload = () => {
        let response = my_request.responseXML;
        if (response != null) {
            add_data_function(workspace_id, response);
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
///<reference path='ajax.ts' />
///<reference path='treedata.ts'/>
// courses tree data
//Major:test
function addCoursesData(workspace_id, response) {
    let majors = response.getElementsByTagName('major');
    for (const major of majors) {
        let major_name = major.getElementsByTagName('major_name')[0].innerHTML;
        addDataList(workspace_id, `Major:${major_name}`);
        let major_categories = major.getElementsByTagName('categories')[0];
        let categories = major_categories.getElementsByTagName('category');
        for (const category of categories) {
            let category_name = category.getElementsByTagName('category_name')[0].innerHTML;
            addDataList(`Major:${major_name}`, `Category:${category_name}`);
            let category_subcategories = category.getElementsByTagName('subcategories')[0];
            let subcategories = category_subcategories.getElementsByTagName('subcategory');
            for (const subcategory of subcategories) {
                let subcategory_name = subcategory.getElementsByTagName('subcategory_name')[0].innerHTML;
                addDataList(`Category:${category_name}`, `Subcategory:${subcategory_name}`);
                let subcategory_note = subcategory.getElementsByTagName('subcategory_data')[0].innerHTML;
                addSpecificData(`Subcategory:${subcategory_name}`, subcategory_note);
                let subcategory_requirements = subcategory.getElementsByTagName('requirements')[0];
                let requirements = subcategory_requirements.getElementsByTagName('requirement');
                for (const requirement of requirements) {
                    let requirement_name = requirement.getElementsByTagName('requirement_name')[0].innerHTML;
                    addDataList(`Subcategory:${subcategory_name}`, `Requirement:${requirement_name}`);
                    let requirement_credit = requirement.getElementsByTagName('requirement_data')[0].innerHTML;
                    addSpecificData(`Requirement:${requirement_name}`, requirement_credit);
                    let requirement_courses = requirement.getElementsByTagName('courses')[0];
                    let courses = requirement_courses.getElementsByTagName('course');
                    for (const course of courses) {
                        let course_name = course.getElementsByTagName('course_name')[0].innerHTML;
                        addDataList(`Requirement:${requirement_name}`, `Course:${course_name}`);
                        let course_credit = course.getElementsByTagName('course_data')[0].innerHTML;
                        addSpecificData(`Course:${course_name}`, course_credit);
                        let course_prereqs = course.getElementsByTagName('prereqs')[0];
                        if (course_prereqs != null) {
                            addDataList(`Course:${course_name}`, `Prereq:${course_name}`);
                            let prereqs = course_prereqs.getElementsByTagName('prereq');
                            for (const prereq of prereqs) {
                                let prereq_name = prereq.getElementsByTagName('prereq_name')[0].innerHTML;
                                addSpecificData(`Prereq:${course_name}`, prereq_name);
                            }
                        }
                        let course_ap = course.getElementsByTagName('ap')[0];
                        if (course_ap != null) {
                            addDataList(`Course:${course_name}`, `Ap:${course_name}`);
                            let tests = course_ap.getElementsByTagName('test');
                            for (const test of tests) {
                                let test_name = test.getElementsByTagName('test_name')[0].innerHTML;
                                addSpecificData(`Ap:${course_name}`, test_name);
                            }
                        }
                    }
                }
            }
        }
    }
}
function updateCoursesData() {
    let workspace_id = 'coursesdata';
    clearData(workspace_id);
    let url_source = '/requestcoursesdata';
    requestAJAX(url_source, workspace_id, addCoursesData);
}
//helperdata
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
/// <reference path="coursesdata.ts" />
document.addEventListener("DOMContentLoaded", () => {
    // displaying tree data 
    let treedata = document.getElementsByClassName("caret");
    for (const toggle of treedata) {
        toggle.addEventListener("click", function () {
            let data = toggle.parentElement.querySelector(".nested");
            toggleIt(data);
            toggle.classList.toggle("caret-down");
        });
    }
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
    let forms = ['majorforms', 'categoryforms', 'subcategoryforms',
        'requirementforms', 'courseforms', 'prereqforms', 'apforms'];
    document.getElementById('refreshcoursesdata').onclick = () => {
        updateCoursesData();
    };
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
});
