/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />
/// <reference path="helperButtons.ts" />

function createCourseBlock(workspace_id:string, course_name:string, credit:string){
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) { return} 
    let course = document.createElement("div");
    course.className = "hstack";
    let name = document.createElement("label");
    name.innerHTML = course_name;
    let value = document.createElement("button");
    value.innerHTML = credit;
    course.appendChild(name);
    course.appendChild(value);
    workspace.appendChild(course);
}

function showTermCourses(){}
function showTranferCourses(){}