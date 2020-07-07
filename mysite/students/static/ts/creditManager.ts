///<reference path='creditAjax.ts' />
///<reference path='toggle.ts' />

function displayForms(forms_to_show:string[]){
    let all_forms:string[] = [
        'Majorformadd','Majorformdelete', 
        'Categoryformadd', 'Categoryformdelete',
        'Subcategoryformadd', 'Subcategoryformdelete',
        'Requirementformadd', 'Requirementformdelete',
        'Courseformadd', 'Courseformdelete',
        'Prereqformadd', 'Prereqformdelete',
        'Apformadd', 'Apformdelete'
    ];
    all_forms.forEach(element => {
       dontShowIt(element);
    });
    forms_to_show.forEach(element => {
        showIt(element);
    });
}

function listMajors(){
    clearWorkSpace('Majors', '#listMajors');
    requestAJAX('/requestmajors/', 'major', 'Majors');
    displayForms(['Majorformadd','Majorformdelete']);
}


function listCategories(){
    clearWorkSpace('Categories', '#listCategories');
    let majors:string[] = retrieveData('Majors'); 
    for (let major_name of majors) {
        let name:string = substituteURLSpace(major_name);
        requestAJAX(`/requestcategories/${name}/`, 'category', 'Categories');
    }
    displayForms(['Categoryformadd', 'Categoryformdelete']);
}


function listSubcategories(){
    clearWorkSpace('Subcategories', '#listSubcategories');
    let categories:string[] = retrieveData('Categories');
    for (let category_name of categories) {
        let name:string = substituteURLSpace(category_name);
        requestAJAX(`/requestsubcategories/${name}/`, 'subcategory', 'Subcategories'); 
    }
    displayForms(['Subcategoryformadd', 'Subcategoryformdelete']);
}


function listRequirements(){
    clearWorkSpace('Requirements', '#listRequirements');
    let subcategories:string[] = retrieveData('Subcategories');
    for (let subcategory_name of subcategories) {
        let name:string = substituteURLSpace(subcategory_name);
        requestAJAX(`/requestrequirements/${name}/`, 'requirement', 'Requirements');
    }
    displayForms(['Requirementformadd', 'Requirementformdelete']);
}


function listCourses(){
    clearWorkSpace('Courses', '#listCourses');
    let requirements:string[] = retrieveData('Requirements');
    for (let requirement_name of requirements) {
        let name:string = substituteURLSpace(requirement_name);
        requestAJAX(`/requestcourses/${name}/`, 'course', 'Courses'); 
    }
    displayForms(['Courseformadd', 'Courseformdelete']);
}


function listPrereqs(){
    clearWorkSpace('Prereqs', '#listPrereqs');
    let courses:string[] = retrieveData('Courses');
    for (let course_name of courses) {
        let name:string = substituteURLSpace(course_name);
        requestAJAX(`/requestprereqs/${name}/`, 'prereq', 'Prereqs'); 
    }
    displayForms(['Prereqformadd', 'Prereqformdelete']);
}


function listAP(){
    clearWorkSpace('Ap', '#listAP');
    let courses:string[] = retrieveData('Courses');
    for (let course_name of courses) {
        let name:string = substituteURLSpace(course_name);
        requestAJAX(`/requestap/${name}/`, 'test', 'Ap');
    }
    displayForms(['Apformadd', 'Apformdelete']);
}



