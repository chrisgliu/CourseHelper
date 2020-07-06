"use strict";
// --- displaying data ---
function clearWorkSpace(workspace_id, header_id) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) {
        return;
    }
    let header = workspace.querySelector(header_id);
    let copy = header.cloneNode(true);
    while (workspace.firstChild) {
        let child = workspace.lastChild;
        if (child != null) {
            workspace.removeChild(child);
        }
    }
    workspace.appendChild(copy);
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
///<reference path='creditAjax.ts' />
function listMajors() {
    clearWorkSpace('Majors', '#listMajors');
    requestAJAX('/requestmajors/', 'major', 'Majors');
}
function listCategories() {
    clearWorkSpace('Categories', '#listCategories');
    let majors = retrieveData('Majors');
    for (let major_name of majors) {
        let name = substituteURLSpace(major_name);
        requestAJAX(`/requestcategories/${name}/`, 'category', 'Categories');
    }
}
function listSubcategories() {
    clearWorkSpace('Subcategories', '#listSubcategories');
    let categories = retrieveData('Categories');
    for (let category_name of categories) {
        let name = substituteURLSpace(category_name);
        requestAJAX(`/requestsubcategories/${name}/`, 'subcategory', 'Subcategories');
    }
}
function listRequirements() {
    clearWorkSpace('Requirements', '#listRequirements');
    let subcategories = retrieveData('Subcategories');
    for (let subcategory_name of subcategories) {
        let name = substituteURLSpace(subcategory_name);
        requestAJAX(`/requestrequirements/${name}/`, 'requirement', 'Requirements');
    }
}
function listCourses() {
    clearWorkSpace('Courses', '#listCourses');
    let requirements = retrieveData('Requirements');
    for (let requirement_name of requirements) {
        let name = substituteURLSpace(requirement_name);
        requestAJAX(`/requestcourses/${name}/`, 'course', 'Courses');
    }
}
function listPrereqs() {
    clearWorkSpace('Prereqs', '#listPrereqs');
    let courses = retrieveData('Courses');
    for (let course_name of courses) {
        let name = substituteURLSpace(course_name);
        requestAJAX(`/requestprereqs/${name}/`, 'prereq', 'Prereqs');
    }
}
function listAP() {
    clearWorkSpace('Ap', '#listAP');
    let courses = retrieveData('Courses');
    for (let course_name of courses) {
        let name = substituteURLSpace(course_name);
        requestAJAX(`/requestap/${name}/`, 'test', 'Ap');
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
