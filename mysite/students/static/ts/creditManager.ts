///<reference path='creditAjax.ts' />

var filter_majors:string[]= [];
var filter_categories:string[] = [];
var filter_subcategories:string[] = [];
var filter_requirements:string[] = [];
var filter_courses:string[] = [];


function listMajors(){
    clearWorkSpace('Majors');
    requestMajors('Majors');
    filter_majors = [];
    let data:string[] = retrieveData('Majors'); 
    data.forEach(element => {
        filter_majors.push(element);
    });
}


function listCategories(){
    clearWorkSpace('Categories');
    for (let major_name of filter_majors) {
        requestCategories('Categories', major_name);
    }
    filter_categories = [];
    let data:string[] = retrieveData('Categories');
    data.forEach(element => {
        filter_categories.push(element);
    });

}


function listSubcategories(){
    clearWorkSpace('Subcategories');
    for (let category_name of filter_categories) {
        requestSubcategories('Subcategories', category_name)
    }
    filter_subcategories = [];
    let data:string[] = retrieveData('Subcategories');
    data.forEach(element => {
        filter_subcategories.push(element);
    });
}


function listRequirements(){
    clearWorkSpace('Requirements');
    for (let subcategory_name of filter_subcategories) {
        requestSubcategories('Requirements', subcategory_name)
    }
    filter_requirements = [];
    let data:string[] = retrieveData('Requirements');
    data.forEach(element => {
        filter_requirements.push(element);
    });
}


function listCourses(){
    clearWorkSpace('Courses');
    for (let requirement_name of filter_requirements) {
        requestSubcategories('Courses', requirement_name)
    }
    filter_courses = []
    let data:string[] = retrieveData('Courses');
    data.forEach(element => {
        filter_courses.push(element);
    });
}


function listPrereqs(){
    clearWorkSpace('Prereqs');
    for (let course_name of filter_courses) {
        requestPrereqs('Prereqs', course_name);
    }
}


function listAP(){
    clearWorkSpace('Ap');
    for (let course_name of filter_courses) {
        requestAP('Ap', course_name);
    }
}



