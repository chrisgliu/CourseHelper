///<reference path='creditAjax.ts' />


function listMajors(){
    clearWorkSpace('Majors', '#listMajors');
    requestAJAX('/requestmajors/', 'major', 'Majors');
}


function listCategories(){
    clearWorkSpace('Categories', '#listCategories');
    let majors:string[] = retrieveData('Majors'); 
    for (let major_name of majors) {
        let name:string = substituteURLSpace(major_name);
        requestAJAX(`/requestcategories/${name}/`, 'category', 'Categories');
    }
}


function listSubcategories(){
    clearWorkSpace('Subcategories', '#listSubcategories');
    let categories:string[] = retrieveData('Categories');
    for (let category_name of categories) {
        let name:string = substituteURLSpace(category_name);
        requestAJAX(`/requestsubcategories/${name}/`, 'subcategory', 'Subcategories'); 
    }
}


function listRequirements(){
    clearWorkSpace('Requirements', '#listRequirements');
    let subcategories:string[] = retrieveData('Subcategories');
    for (let subcategory_name of subcategories) {
        let name:string = substituteURLSpace(subcategory_name);
        requestAJAX(`/requestrequirements/${name}/`, 'requirement', 'Requirements');
    }
}


function listCourses(){
    clearWorkSpace('Courses', '#listCourses');
    let requirements:string[] = retrieveData('Requirements');
    for (let requirement_name of requirements) {
        let name:string = substituteURLSpace(requirement_name);
        requestAJAX(`/requestcourses/${name}/`, 'course', 'Courses'); 
    }
}


function listPrereqs(){
    clearWorkSpace('Prereqs', '#listPrereqs');
    let courses:string[] = retrieveData('Courses');
    for (let course_name of courses) {
        let name:string = substituteURLSpace(course_name);
        requestAJAX(`/requestprereqs/${name}/`, 'prereq', 'Prereqs'); 
    }
}


function listAP(){
    clearWorkSpace('Ap', '#listAP');
    let courses:string[] = retrieveData('Courses');
    for (let course_name of courses) {
        let name:string = substituteURLSpace(course_name);
        requestAJAX(`/requestap/${name}/`, 'test', 'Ap');
    }
}



