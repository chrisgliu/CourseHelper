/// <reference path="ajaxForm.ts" />

function semesterAJAX(sub_url_request:string, semesters:string[], year:string){
    for (const semester of semesters) {
        $.ajax({
            url:sub_url_request,
            type:"POST",
            data:{"year":`${year}`, "semester":semester},
            dataType:"json",
            beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
            },
            success: function (){},
            error: function (){}
        });        
    }   
}
function yearAJAX(url_request:string, year:string){
    $.ajax({
        url:url_request,
        type:"POST",
        data:{"year":`${year}`},
        dataType:"json",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
        },
        success: function (){},
        error: function (){}
    });
}

function makeSemesters(year:string, terms:string, startingindex:number=1, add_or_delete:string){
    let semesters:string[] = [];
    if(add_or_delete == "add"){
        for (let index = startingindex; index < startingindex+parseInt(terms); index++) {
            let semester = `${year}:TERM-${index}`;
            semesters.push(semester);
        }
    }
    if(add_or_delete == "delete"){
        for (let index = startingindex; index > startingindex-parseInt(terms); index--) {
            let semester = `${year}:TERM-${index}`;
            semesters.push(semester);
        }
    }
    return semesters;
}
function getLatestYearID(){
    let list:HTMLUListElement = (<HTMLUListElement>document.getElementById("plannerdata"));
    let header = list.getElementsByTagName("span");
    let years:string[] = [];
    let year_in_question = "";
    for (const element of header) {
        let id = element.id;
        if (id.indexOf("YEAR")!=-1){
            years.push(id);
        }
    }
    year_in_question = years[years.length-1];
    for (const year_id of years) {
        let symbol = document.getElementById(year_id);
        if (symbol.className == "caret caret-down"){
            year_in_question = year_id
        }
    }
    let year_value = year_in_question.substring(year_in_question.indexOf("-")+1);
    return year_value;
}
function activateYearManager(){
    document.getElementById("addbuttonyearmanager").onclick = ()=> {
        let startingyear = (<HTMLInputElement>document.getElementById("startingyear")).value;
        let yearnum = document.getElementById("plannerdata").children.length;
        if (yearnum == 0){
            yearAJAX("/addMyYear", startingyear);
        }
        if (yearnum >= 1){
            let year = `${parseInt(startingyear) + (yearnum)}`;
            yearAJAX("/addMyYear", year);
        }
    }
    document.getElementById("deletebuttonyearmanager").onclick = ()=> {
        let year_id = getLatestYearID()
        let year = year_id.substring(year_id.indexOf(":")+1);
        if (year != null){
            yearAJAX("/deleteMyYear", year); 
        }
    }
    document.getElementById("addbuttonsemestermanager").onclick = ()=> {
        let terms = (<HTMLInputElement>document.getElementById("termsperyear")).value;
        let year = getLatestYearID();
        let index = document.getElementById(year).children.length+1;
        if (year != null){
            let year_val = year.substring(year.indexOf(":")+1);
            let semesters = makeSemesters(year_val, terms, index, "add");
            semesterAJAX("/addMySemester", semesters, year_val);
        }
    }
    document.getElementById("deletebuttonsemestermanager").onclick = ()=> {
        let terms = (<HTMLInputElement>document.getElementById("termsperyear")).value;
        let year = getLatestYearID();
        let index = document.getElementById(year).children.length;
        if (year != null){
            let year_val = year.substring(year.indexOf(":")+1);
            let semesters = makeSemesters(year_val, terms, index, "delete");
            semesterAJAX("/deleteMySemester", semesters, year_val);
        }
    }
}

function updatemajormanageroptionsmajors() {
    addSelectionOptions("majormanageroptionsmajors", getSessionData("major"));
}
function activateMajorManagerAdd(){
    updatemajormanageroptionsmajors();
    activateTHISForm("majormanageraddbutton", "/addMyMajor",
       null, null,
       ["majormanageroptionsmajors"], 
       [["major"]],
       updatemajormanageroptionsmajors
    );
}
function activateMajorManagerDelete(){
    updatemajormanageroptionsmajors();
    activateTHISForm("majormanagerdeletebutton", "/deleteMajor",
       null, null,
       ["majormanageroptionsmajors"], 
       [["major"]],
       updatemajormanageroptionsmajors
    );
}

function updatecoursemanageroptions() {
    addSelectionOptions("coursemanageroptionscourse", getSubSessionData("course"));
    addSelectionOptions("coursemanageroptionsterms", getSessionData("mysemester"))
}
function activateCourseManagerAdd(){
    updatecoursemanageroptions();
    activateTHISForm("coursemanageraddbutton", "/addMyCourse",
       null, null,
       ["coursemanageroptionscourse", "coursemanageroptionsterms"], 
       [[null, null, null, null, "course" ],
        ["year", "semester"]],
       updatecoursemanageroptions
    );
}
function activateCourseManagerDelete(){
    updatecoursemanageroptions();
    activateTHISForm("coursemanagerdeletebutton", "/deleteMyCourse",
        null, null,
        ["coursemanageroptionscourse", "coursemanageroptionsterms"], 
        [[null, null, null, null, "course" ],
         ["year", "semester"]],
        updatecoursemanageroptions
    );
}

function inarray(list:any[], value:any){
    if(list == null){return false; }
    for (const item of list) {
        if(item == value){ return true;}
    }
    return false;
}
function updatetestmanageroptionstests() {
    let ap_data = getSessionData("ap");
    if (ap_data == null) {return}
    let ap:string[] = [];
    for (const instance of ap_data) {
        let data = readMySessionString(instance);
        let test_name:string = data[data.length - 3];
        if (!inarray(ap, test_name)){ ap.push(test_name);}
    }
    addSelectionOptions("testmanageroptionstests", ap);
}
function activateTestManagerAdd(){
    updatetestmanageroptionstests();
    activateTHISForm("testmanageraddbutton", "/addMyAP",
       ["testmanagerscore"],
       ["score"], 
       ["testmanageroptionstests"], 
       [["test_name"]],
       updatetestmanageroptionstests
    );
 }
function activateTestManagerDelete(){
    updatetestmanageroptionstests();
    activateTHISForm("testmanagerdeletebutton", "/deleteMyAP",
       ["testmanagerscore"],
       ["score"], 
       ["testmanageroptionstests"], 
       [["test_name"]],
       updatetestmanageroptionstests
    );
 }

function activateHelperForms() {
    activateYearManager();
    activateMajorManagerAdd();
    activateMajorManagerDelete();
    activateCourseManagerAdd();
    activateCourseManagerDelete();
    activateTestManagerAdd();
    activateTestManagerDelete();
}
