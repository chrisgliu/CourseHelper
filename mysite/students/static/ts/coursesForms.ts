/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />

function activateForm(submit_button_id:string, request_url:string,
                      inputs:string[], input_breakdown:string[],
                      options:string[], option_breakdown:string[][]){
    document.getElementById(submit_button_id).onclick = ()=>{
        let request = new XMLHttpRequest();
        request.open("POST", request_url, true);
        request.setRequestHeader('Content-Type', 'application/json');
        let data:{ [input:string]: string; } = {};
        if (options != null) {
           for (let index = 0; index < options.length; index++) {
              const selector = options[index];
              const selector_breakdown = option_breakdown[index];
              let values = getSelectionValue(selector);
              let value_list = readMySessionString(values);
              for (let v_index = 0; v_index < value_list.length; v_index++) {
                const value = value_list[v_index];
                const tag = selector_breakdown[v_index];
                data[tag] = value;
              }  
            }
        }
        if (inputs != null){
          for (let index = 0; index < inputs.length; index++) {
            const input = inputs[index];
            let value = getInputValue(input);
            let tag = input_breakdown[index];
            data[tag] = value;
          }
        }
        let token = (<HTMLInputElement> document.getElementById("hiddenform").childNodes[0]).value;
        alert(token)
        data["csrfmiddlewaretoken"] = token;
        request.send(JSON.stringify(data));
    }
}
function activateMajorFormA(){
    activateForm("majorcreatebutton", 
               "/courses/createmajor", 
               ["majorFormAmajor"],
               ["major"],
               null,
               null
              ); 
}
function activateMajorFormB(){
    let majors = getSessionData("major");
    addSelectionOptions("majorFormBoptionsmajors", majors);

    activateForm("majordeletebutton",
               "/courses/deletemajor",
               null,
               null,
               ["majorFormBoptionsmajors"],
               [["major"]],
              );
}

function activateCategoryFormA(){
    let majors = getSessionData("major");
    addSelectionOptions("categoryFormAoptionsmajors", majors);

    activateForm("categorycreatebutton",
               "/courses/createcategory",
               ["categoryFormAcategory"], 
               ["category"],
               ["categoryFormAoptionsmajors"],
               [["major"]]
              );
}
function activateCategoryFormB(){
     let categories = getSessionData("category");
     addSelectionOptions("categoryFormBoptionscategories", categories);

     activateForm("categoryaddbutton", 
                 "/courses/createcategory",
                 null,
                 null,
                 ["categoryFormBoptionscategories"],
                 [["major", "category"]]
                );
     activateForm("categorydeletebutton", 
                 "/courses/deletecategory",
                 null,
                 null,
                 ["categoryFormBoptionscategories"],
                 [["major", "category"]]
                );

}
function activateSubcategoryFormA(){
    let categories = getSessionData("category");
    addSelectionOptions("subcategoryFormAoptionscategories", categories);

    activateForm("subcategorycreatebutton", 
                 "/courses/createsubcategory",
                 ["subcategoryFormAsubcategory", "subcategoryFormAnote"],
                 ["subcategory", "note"],
                 ["subcategoryFormAoptionscategories"],
                 [["major", "category"]]
                );
}
function activateSubcategoryFormB(){
    let subcategories_data = getSessionData("subcategory");
    let subcategories:string[] = [];
    for (const subcategory of subcategories_data) {
      subcategories.push(subcategory[0]);
    }
    addSelectionOptions("subcategoryFormBoptionssubcategories", subcategories);

    activateForm("subcategoryaddbutton", 
                 "/courses/createsubcategory",
                 null,
                 null,
                 ["subcategoryFormBoptionssubcategories"],
                 [["major", "category", "subcategory"]]
                );
    activateForm("subcategorydeletebutton", 
                 "/courses/deletesubcategory",
                 null,
                 null,
                 ["subcategoryFormBoptionssubcategories"],
                 [["major", "category", "subcategory"]]
                );
}
function activateRequirementFormA(){
    let subcategories_data = getSessionData("subcategory");
    let subcategories:string[] = [];
    for (const subcategory of subcategories_data) {
      subcategories.push(subcategory[0]);
    }
    addSelectionOptions("requirementFormAoptionssubcategories", subcategories);

    activateForm("requirementaddbutton", 
                 "/courses/createrequirement",
                 ["requirementFormArequirement", "requirementFormAcredit"],
                 ["requirement", "credit"],
                 ["requirementFormAoptionssubcategories"],
                 [["major", "category", "subcategory"]]
                );


}
function activateRequirementFormB(){
    let requirements_data = getSessionData("requirement");
    let requirements:string[] = [];
    for (const requirement of requirements_data) {
      requirements.push(requirement[0]);
    }
    addSelectionOptions("requirementFormBoptionsrequirements", requirements);

    activateForm("requirementaddbutton", 
                 "/courses/createrequirement",
                 null,
                 null,
                 ["requirementFormBoptionsrequirements"],
                 [["major", "category", "subcategory", "requirement"]]
                );
    activateForm("requirementdeletebutton", 
                 "/courses/deleterequirement",
                 null,
                 null,
                 ["requirementFormBoptionsrequirements"],
                 [["major", "category", "subcategory", "requirement"]]
                );

}
function activateCourseFormA(){
   let requirements_data = getSessionData("requirement");
   let requirements:string[] = [];
   for (const requirement of requirements_data) {
      requirements.push(requirement[0]);
   }
   addSelectionOptions("courseFormAoptionsrequirements", requirements);

    activateForm("coursecreatebutton", 
                 "/courses/createcourse",
                 ["courseFormAcourse", "courseFormAcredit"],
                 ["course", "credit"],
                 ["courseFormAoptionsrequirements"],
                 [["major", "category", "subcategory", "requirement"]]
                );
}
function activateCourseFormB(){
    let courses_data = getSessionData("course");
    let courses:string[] = [];
    for (const course of courses_data) {
      courses.push(course[0]);
    }
    addSelectionOptions("courseFormBoptionscourses", courses);

    activateForm("courseaddbutton", 
                 "/courses/createcourse",
                 null,
                 null,
                 ["courseFormBoptionscourses"],
                 [["major", "category", "subcategory", "requirement", "course" ]]
                );
    activateForm("coursedeletebutton", 
                 "/courses/deletecourse",
                 null,
                 null,
                 ["courseFormBoptionscourses"],
                 [["major", "category", "subcategory", "requirement", "course" ]]
                );
}
function activatePrereqForms() {
    let courses_data = getSessionData("course");
    let courses:string[] = [];
    for (const course of courses_data) {
       courses.push(course[0]);
    }
    addSelectionOptions("prereqFormAoptionscourses", courses);
    addSelectionOptions("prereqFormAoptionsprereqs", courses)
    // cant be the same course
    activateForm("prereqaddbutton", 
                 "/courses/createprereq",
                 null,
                 null,
                 ["prereqFormAoptionscourses", "prereqFormAoptionsprereqs"],
                 [["major", "category", "subcategory", "requirement", "course"],
                   ["pmajor", "pcategory", "psubcategory", "prequirement", "pcourse"]]
                );
    activateForm("prereqdeletebutton", 
                 "/courses/deleteprereq",
                 null,
                 null,
                 ["prereqFormAoptionscourses", "prereqFormAoptionsprereqs"],
                 [["major", "category", "subcategory", "requirement", "course"],
                   ["pmajor", "pcategory", "psubcategory", "prequirement", "pcourse"]]
                );
}
function activateAPFormA(){
    let courses_data = getSessionData("course");
    let courses:string[] = [];
    for (const course of courses_data) {
       courses.push(course[0]);
    };
    addSelectionOptions("apFormAoptionscourses", courses);
    activateForm("apcreatebutton", 
                 "/courses/createap",
                 ["apFormAtest", "apFormAmin", "apFormAmax"],
                 ["test", "scoremin", "scoremax"],
                 ["apFormAoptionscourses"],
                 [["major", "category", "subcategory", "requirement", "course"]]
                );
}
function activateAPFormB(){
    let courses_data = getSessionData("course");
    let courses:string[] = [];
    for (const course of courses_data) {
       courses.push(course[0]);
    }
    addSelectionOptions("apFormBoptionscourses", courses);
    let tests = getSessionData("test");
    addSelectionOptions("apFormBoptionstests", tests);

    activateForm("apaddbutton", 
                 "/courses/createap",
                 null,
                 null,
                 ["apFormBoptionstests", "apFormBoptionscourses"],
                 [["test", "scoremin", "scoremax"],
                   ["major", "category", "subcategory", "requirement", "course"]]
                );
    activateForm("apdeletebutton", 
                 "/courses/deleteap",
                 null,
                 null,
                 ["apFormBoptionstests", "apFormBoptionscourses"],
                 [["test", "scoremin", "scoremax"],
                   ["major", "category", "subcategory", "requirement", "course"]]
                );
}



