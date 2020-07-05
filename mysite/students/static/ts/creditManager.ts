///<reference path='creditAjax.ts' />

function listMajors(){
    clearWorkSpace('Majors')
    requestMajors('Majors')
}
function listCategories(){
    clearWorkSpace('Categories')
    requestCategories('Categories', major_name)
}
function listSubcategories(){
    clearWorkSpace('Subcategories') 
    requestSubcategories('Subcategories', category_name)
}
function listRequirements(){
    clearWorkSpace('Requirements')
    requestRequirements('Requirements', subcategory_name)
}
function listCourses(){
    clearWorkSpace('Courses')
    requestCourses('Courses', requirement_name)
}
function listPrereqs(){
    clearWorkSpace('Prereqs')
    requestPrereqs('Prereqs', course_name)
}
function listAP(){
    clearWorkSpace('Ap')
    requestAP('Ap', course_name)
}



