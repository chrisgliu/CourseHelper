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
function readXMLData(workspace_id, xml_data, data_tag) {
    let data = xml_data.getElementsByTagName(data_tag);
    for (let data_instance of data) {
        let info = data_instance.innerHTML;
        addData(workspace_id, info);
    }
}
// --- making a request for data ---
function requestAJAX(url_source, data_tag, work_space_id) {
    let request = new XMLHttpRequest();
    request.open('GET', url_source, true);
    request.onload = () => {
        let response = request.responseXML;
        if (response != null) {
            readXMLData(work_space_id, response, data_tag);
        }
    };
    request.send();
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
function listMajors() {
    clearWorkSpace('Majors');
    requestMajors('Majors');
}
function listCategories(major_name) {
    clearWorkSpace('Categories');
    requestCategories('Categories', major_name);
}
function listSubcategories(category_name) {
    clearWorkSpace('Subcategories');
    requestSubcategories('Subcategories', category_name);
}
function listRequirements(subcategory_name) {
    clearWorkSpace('Requirements');
    requestRequirements('Requirements', subcategory_name);
}
function listCourses(requirement_name) {
    clearWorkSpace('Courses');
    requestCourses('Courses', requirement_name);
}
function listPrereqs(course_name) {
    clearWorkSpace('Prereqs');
    requestPrereqs('Prereqs', course_name);
}
function listAP(course_name) {
    clearWorkSpace('Ap');
    requestAP('Ap', course_name);
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
