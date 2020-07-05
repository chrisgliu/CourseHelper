///<reference path='creditAjax.ts' />

function listMajors(){
    clearWorkSpace('Majors')
    requestMajors('Majors')
}
function listCategories(major_name:string){
    clearWorkSpace('Categories')
    requestCategories('Categories', major_name)
}
function listSubcategories(category_name:string){
    clearWorkSpace('Subcategories') 
    requestSubcategories('Subcategories', category_name)
}
function listRequirements(subcategory_name:string){
    clearWorkSpace('Requirements')
    requestRequirements('Requirements', subcategory_name)
}
function listCourses(requirement_name:string){
    clearWorkSpace('Courses')
    requestCourses('Courses', requirement_name)
}
function listPrereqs(course_name:string){
    clearWorkSpace('Prereqs')
    requestPrereqs('Prereqs', course_name)
}
function listAP(course_name:string){
    clearWorkSpace('Ap')
    requestAP('Ap', course_name)
}



