"use strict";
// --- displaying data ---
function clearWorkSpace(workspace_id) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) {
        return;
    }
    while (workspace.firstChild) {
        let child = workspace.lastChild;
        if (child != null) {
            workspace.removeChild(child);
        }
    }
    let header = document.createElement('th');
    header.innerHTML = workspace_id;
    workspace.appendChild(header);
}
function addData(workspace_id, info) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) {
        return;
    }
    let data = document.createElement('td');
    data.innerHTML = info;
    workspace.appendChild(data);
}
// --- making a request for data ---
function requestAJAX(url_source, data_tag, workspace_id) {
    let request = new XMLHttpRequest();
    request.open('GET', url_source, true);
    request.onload = () => {
        let response = request.responseXML;
        if (response != null) {
            let data = response.getElementsByTagName(data_tag);
            for (let data_instance of data) {
                let info = data_instance.innerHTML;
                addData(workspace_id, info);
            }
        }
    };
    request.send();
    // cant return value in asynchronous request
}
function substituteChar(message, spot, item) {
    let before = message.substring(0, spot);
    let after = message.substring(spot + 1);
    let result = before + item + after;
    return result;
}
function substituteURLSpace(message) {
    let edited_message = message;
    for (let index = 0; index < message.length; index++) {
        let char = message.charAt(index);
        if (char == ' ') {
            edited_message = substituteChar(edited_message, index, '%20');
        }
    }
    return edited_message;
}
// retrieving listed data
function retrieveData(workspace_id) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) {
        return;
    }
    let info_list = [];
    let data = workspace.children;
    for (let index = 1; index < data.length; index++) {
        const info = data[index].innerHTML;
        info_list.push(info);
    }
    return info_list;
}
// --- request functions ---
function requestMajors(workspace_id) {
    requestAJAX('/requestmajors/', 'major', workspace_id);
}
function requestCategories(workspace_id, parent_name) {
    let name = substituteURLSpace(parent_name);
    requestAJAX(`/requestcategories/${name}/`, 'category', workspace_id);
}
function requestSubcategories(workspace_id, parent_name) {
    let name = substituteURLSpace(parent_name);
    requestAJAX(`/requestsubcategories/${name}/`, 'subcategory', workspace_id);
}
function requestRequirements(workspace_id, parent_name) {
    let name = substituteURLSpace(parent_name);
    requestAJAX(`/requestrequirements/${name}/`, 'requirement', workspace_id);
}
function requestCourses(workspace_id, parent_name) {
    let name = substituteURLSpace(parent_name);
    requestAJAX(`/requestcourses/${name}/`, 'course', workspace_id);
}
function requestPrereqs(workspace_id, parent_name) {
    let name = substituteURLSpace(parent_name);
    requestAJAX(`/requestprereqs/${name}/`, 'prereq', workspace_id);
}
function requestAP(workspace_id, parent_name) {
    let name = substituteURLSpace(parent_name);
    requestAJAX(`/requestap/${name}/`, 'test', workspace_id);
}
///<reference path='creditAjax.ts' />
var filter_majors = [];
var filter_categories = [];
var filter_subcategories = [];
var filter_requirements = [];
var filter_courses = [];
function listMajors() {
    clearWorkSpace('Majors');
    requestMajors('Majors');
    filter_majors = [];
    let data = retrieveData('Majors');
    data.forEach(element => {
        filter_majors.push(element);
    });
}
function listCategories() {
    clearWorkSpace('Categories');
    for (let major_name of filter_majors) {
        requestCategories('Categories', major_name);
    }
    filter_categories = [];
    let data = retrieveData('Categories');
    data.forEach(element => {
        filter_categories.push(element);
    });
}
function listSubcategories() {
    clearWorkSpace('Subcategories');
    for (let category_name of filter_categories) {
        requestSubcategories('Subcategories', category_name);
    }
    filter_subcategories = [];
    let data = retrieveData('Subcategories');
    data.forEach(element => {
        filter_subcategories.push(element);
    });
}
function listRequirements() {
    clearWorkSpace('Requirements');
    for (let subcategory_name of filter_subcategories) {
        requestSubcategories('Requirements', subcategory_name);
    }
    filter_requirements = [];
    let data = retrieveData('Requirements');
    data.forEach(element => {
        filter_requirements.push(element);
    });
}
function listCourses() {
    clearWorkSpace('Courses');
    for (let requirement_name of filter_requirements) {
        requestSubcategories('Courses', requirement_name);
    }
    filter_courses = [];
    let data = retrieveData('Courses');
    data.forEach(element => {
        filter_courses.push(element);
    });
}
function listPrereqs() {
    clearWorkSpace('Prereqs');
    for (let course_name of filter_courses) {
        requestPrereqs('Prereqs', course_name);
    }
}
function listAP() {
    clearWorkSpace('Ap');
    for (let course_name of filter_courses) {
        requestAP('Ap', course_name);
    }
}
function toggleShow(id) {
    let element = document.getElementById(id);
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
