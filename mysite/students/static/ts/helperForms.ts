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
function yearAJAXa(url_request:string, startingyear:string){
    yearAJAX(url_request, "before");
    yearAJAX(url_request, startingyear);
}
function yearAJAXb(url_request:string, year:string){
    yearAJAX(url_request, year);
}

function makeSemesters(year:string, terms:string, startingindex:number=1, add_or_delete:string){
    let semesters:string[] = [];
    if(add_or_delete == "add"){
        for (let index = startingindex; index < startingindex+parseInt(terms); index++) {
            let semester = `${year}:Term-${index}`;
            semesters.push(semester);
        }
    }
    if(add_or_delete == "delete"){
        for (let index = startingindex; index > startingindex-parseInt(terms); index--) {
            let semester = `${year}:Term-${index}`;
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
            //create before and starting year
            yearAJAXa("/addMyYear", startingyear);
        }
        if (yearnum == 1){
            yearAJAXb("/addMyYear", startingyear); 
        }
        if (yearnum >= 2){

            let year = `${parseInt(startingyear) + (yearnum-2) + 1}`;
            yearAJAXb("/addMyYear", year);
        }
    }
    document.getElementById("deletebuttonyearmanager").onclick = ()=> {
        let year_id = getLatestYearID()
        let year = year_id.substring(year_id.indexOf(":")+1);
        if (year != null){
            yearAJAXa("/deleteMyYear", year); 
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

function updatecoursemanageroptionscourses() {
    addSelectionOptions("coursemanageroptionscourse", getSubSessionData("course"));
}
function activateCourseManagerAdd(){
    updatecoursemanageroptionscourses();
    activateTHISForm("coursemanageraddbutton", "/addMyCourse",
       null, null,
       ["coursemanageroptionscourse"], 
       [["major", "category", "subcategory", "requirement", "course" ]],
       updatecoursemanageroptionscourses
    );
}
function activateCourseManagerDelete(){
    updatecoursemanageroptionscourses();
    activateTHISForm("coursemanagerdeletebutton", "/deleteMyCourse",
       null, null,
       ["coursemanageroptionscourse"], 
       [["major", "category", "subcategory", "requirement", "course" ]],
       updatecoursemanageroptionscourses
    );
}

function updatetestmanageroptionstests() {
    addSelectionOptions("testmanageroptionstests", getSessionData("ap"));
}
function activateTestManagerAdd(){
    updatetestmanageroptionstests();
    activateTHISForm("testmanageraddbutton", "/addMyAP",
       null, null,
       ["testmanageroptionstests"], 
       [["major", "category", "subcategory", "requirement", "course", "skip", "test", "scoremin", "scoremax"]],
       updatetestmanageroptionstests
    );
 }
function activateTestManagerDelete(){
    updatetestmanageroptionstests();
    activateTHISForm("testmanagerdeletebutton", "/deleteMyAP",
       null, null,
       ["testmanageroptionstests"], 
       [["major", "category", "subcategory", "requirement", "course", "skip", "test", "scoremin", "scoremax"]],
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
