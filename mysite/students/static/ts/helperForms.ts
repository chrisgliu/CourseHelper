/// <reference path="ajaxForm.ts" />

function yearAJAXa(url_request:string, sub_url_request:string, startingyear:string, semesters:string[]){
    $.ajax(
        {
            url:url_request,
            type:"POST",
            data:{"year":"before"},
            dataType:"json",
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
            },
            success: function (){},
            error: function (){}
        }
    );
    $.ajax(
        {
            url:url_request,
            type:"POST",
            data:{"year":`${startingyear}`},
            dataType:"json",
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
            },
            success: function (){},
            error: function (){}
        }
    );
    for (const semester of semesters) {
        $.ajax(
            {
                url:sub_url_request,
                type:"POST",
                data:{"year":`${startingyear}`, "semester":semester},
                dataType:"json",
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
                },
                success: function (){},
                error: function (){}
            }
        );
    }
}
function yearAJAXb(url_request:string, sub_url_request:string, year:string, semesters:string[]){
    $.ajax(
        {
            url:url_request,
            type:"POST",
            data:{"year":`${year}`},
            dataType:"json",
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
            },
            success: function (){},
            error: function (){}
        }
    );
    for (const semester of semesters) {
        $.ajax(
            {
                url:sub_url_request,
                type:"POST",
                data:{"year":`${year}`, "semester":semester},
                dataType:"json",
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type)) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));}
                },
                success: function (){},
                error: function (){}
            }
        );
    }
}

function makeSemesters(year:string, termsperyear:string){
    let semesters:string[] = [];
    for (let index = 1; index <= parseInt(termsperyear); index++) {
        let semester = `${year}:Term-${index}`;
        semesters.push(semester);
    }
    return semesters;
}
function activateYearManager(){
    document.getElementById("addbuttonyearmanager").onclick = ()=> {
        let termsperyear = (<HTMLInputElement>document.getElementById("termsperyear")).value;
        let startingyear = (<HTMLInputElement>document.getElementById("startingyear")).value;
        let yearnum = document.getElementById("plannerdata").children.length;
        if (yearnum == 0){
            //create before and starting year
            let semesters = makeSemesters(startingyear, termsperyear)
            yearAJAXa("/addMyYear", "/addMySemester", startingyear, semesters);
        }
        if (yearnum > 2){
            let time = yearnum-2;
            let year = `${parseInt(startingyear) + time}`;
            let semesters = makeSemesters(year, termsperyear)
            yearAJAXb("/deleteMyYear", "/deleteMySemester", year, semesters);
        }
    }
    document.getElementById("deletebuttonyearmanager").onclick = ()=> {
        let termsperyear = (<HTMLInputElement>document.getElementById("termsperyear")).value;
        let startingyear = (<HTMLInputElement>document.getElementById("startingyear")).value;
        let yearnum = document.getElementById("plannerdata").children.length;
        if (yearnum == 0){return;}
        if (yearnum == 2){
            //delete before and starting year
            let semesters = makeSemesters(startingyear, termsperyear)
            yearAJAXa("/addMyYear", "/addMySemester", startingyear, semesters);
        }
        if (yearnum > 2){
            let time = yearnum-2;
            let year = `${parseInt(startingyear) + time}`
            let semesters = makeSemesters(year, termsperyear)
            yearAJAXb("/deleteMyYear", "/deleteMySemester", year, semesters);
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
