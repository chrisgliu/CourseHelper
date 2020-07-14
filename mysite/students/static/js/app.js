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
///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
// courses tree data
class content {
    constructor(tag_a, tag_b, tag_c) {
        this.key_a = tag_a;
        this.key_b = tag_b;
        this.key_c = tag_c;
        this.value_a = this.value_b = this.value_c = null;
    }
    set assignValA(value) { this.value_a = value; }
    set assignValB(value) { this.value_b = value; }
    set assignValC(value) { this.value_c = value; }
    valueOf(key) {
        if (key == this.key_a) {
            return this.value_a;
        }
        if (key == this.key_b) {
            return this.value_b;
        }
        if (key == this.key_c) {
            return this.value_c;
        }
    }
}
function readNodeContent(node_content, tag_a, tag_b, tag_c) {
    let output = new content(tag_a, tag_b, tag_c);
    for (const node of node_content) {
        if (node.nodeType == 1) {
            if (node.nodeName == tag_a) {
                output.assignValA = node;
            }
            if (node.nodeName == tag_b) {
                output.assignValB = node;
            }
            if (node.nodeName == tag_c) {
                output.assignValC = node;
            }
        }
    }
    return output;
}
//Major:test
function addCoursesData(workspace_id, response) {
    let majors = response.getElementsByTagName('major');
    for (const major of majors) {
        let major_content = readNodeContent(major.childNodes, 'major_name', 'categories', null);
        let major_name = major_content.valueOf('major_name').nodeValue;
        addDataList(workspace_id, `Major:${major_name}`);
        let categories_node = major_content.valueOf('categories');
        let categories = categories_node.childNodes;
        for (const category of categories) {
            let category_content = readNodeContent(category.childNodes, 'category_name', 'subcategories', null);
            let category_name = category_content.valueOf('category_name').nodeValue;
            addDataList(`Major:${major_name}`, `Category:${category_name}`);
            let subcategories_node = category_content.valueOf('subcategories');
            let subcategories = subcategories_node.childNodes;
            for (const subcategory of subcategories) {
                let subcategory_content = readNodeContent(subcategory.childNodes, 'subcategory_name', 'requirements', null);
                let subcategory_name = subcategory_content.valueOf('subcategory_name').nodeValue;
                addDataList(`Subcategory:${subcategory_name}`, `Category:${category_name}`);
                let requirements_node = subcategory_content.valueOf('requirements');
                let requirements = requirements_node.childNodes;
                for (const requirement of requirements) {
                    let requirement_content = readNodeContent(requirement.childNodes, 'requirement_name', 'courses', null);
                    let requirement_name = requirement_content.valueOf('requirement_name').nodeValue;
                    addDataList(`Subcategory:${subcategory_name}`, `Requirement:${requirement_name}`);
                    let courses_node = requirement_content.valueOf('courses');
                    let courses = courses_node.childNodes;
                    for (const course of courses) {
                        let course_content = readNodeContent(course.childNodes, 'course_name', 'prereqs', 'ap');
                        let course_name = course_content.valueOf('course_name').nodeValue;
                        addDataList(`Requirement:${requirement_name}`, `Course:${course_name}`);
                        let prereqs_node = course_content.valueOf('prereqs');
                        let prereqs = prereqs_node.childNodes;
                        addDataList(`Course:${course_name}`, `Prereq:${course_name}`);
                        for (const prereq of prereqs) {
                            let prereq_content = readNodeContent(prereq.childNodes, 'prereq_name', null, null);
                            let prereq_name = prereq_content.valueOf('prereq_name').nodeValue;
                            addSpecificData(`Prereq:${course_name}`, prereq_name);
                        }
                        let ap_node = course_content.valueOf('ap');
                        let ap = ap_node.childNodes;
                        addDataList(`Course:${course_name}`, `Ap:${course_name}`);
                        for (const test of ap) {
                            let test_content = readNodeContent(test.childNodes, 'test_name', null, null);
                            let test_name = test_content.valueOf('test_name').nodeValue;
                            addSpecificData(`Ap:${course_name}`, test_name);
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
