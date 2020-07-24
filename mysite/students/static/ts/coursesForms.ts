/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />
/// <reference path="ajaxForm.ts" />


function activateMajorFormA(){
    activateTHISForm("majorcreatebutton", 
               "/courses/createmajor", 
               ["majorFormAmajor"],
               ["major"],
               null,
               null,
               null
              ); 
}

function updatemajorFormBoptionsmajors() {
   let majors = getSessionData("major");
   addSelectionOptions("majorFormBoptionsmajors", majors);
}
function activateMajorFormB(){
   updatemajorFormBoptionsmajors();
   activateTHISForm("majordeletebutton",
               "/courses/deletemajor",
               null,
               null,
               ["majorFormBoptionsmajors"],
               [["major"]],
               updatemajorFormBoptionsmajors
              );
}

function updatecategoryFormAoptionsmajors(){
   let majors = getSessionData("major");
   addSelectionOptions("categoryFormAoptionsmajors", majors);
}
function activateCategoryFormA(){
   updatecategoryFormAoptionsmajors();
   activateTHISForm("categorycreatebutton",
               "/courses/createcategory",
               ["categoryFormAcategory"], 
               ["category"],
               ["categoryFormAoptionsmajors"],
               [["major"]],
               updatecategoryFormAoptionsmajors
              );
}

function updatecategoryFormBoptionscategories(){
   let categories = getSessionData("category");
   addSelectionOptions("categoryFormBoptionscategories", categories);
}
function activateCategoryFormB(){
   updatecategoryFormBoptionscategories();
   activateTHISForm("categoryaddbutton", 
                 "/courses/createcategory",
                 null,
                 null,
                 ["categoryFormBoptionscategories"],
                 [["major", "category"]],
                 updatecategoryFormBoptionscategories
                );
   activateTHISForm("categorydeletebutton", 
                 "/courses/deletecategory",
                 null,
                 null,
                 ["categoryFormBoptionscategories"],
                 [["major", "category"]],
                 updatecategoryFormBoptionscategories
                );
}
function updatesubcategoryFormAoptionscategories(){
   let categories = getSessionData("category");
   addSelectionOptions("subcategoryFormAoptionscategories", categories);
}
function activateSubcategoryFormA(){
   updatesubcategoryFormAoptionscategories();
   activateTHISForm("subcategorycreatebutton", 
                 "/courses/createsubcategory",
                 ["subcategoryFormAsubcategory", "subcategoryFormAnote"],
                 ["subcategory", "note"],
                 ["subcategoryFormAoptionscategories"],
                 [["major", "category"]],
                 updatesubcategoryFormAoptionscategories
                );
}
function updatesubcategoryFormBoptionssubcategories(){
   let subcategories_data = getSessionData("subcategory");
   let subcategories:string[] = [];
   for (const subcategory of subcategories_data) {
     subcategories.push(subcategory[0]);
   }
   addSelectionOptions("subcategoryFormBoptionssubcategories", subcategories);
}
function activateSubcategoryFormB(){
   updatesubcategoryFormBoptionssubcategories();
   activateTHISForm("subcategoryaddbutton", 
                 "/courses/createsubcategory",
                 null,
                 null,
                 ["subcategoryFormBoptionssubcategories"],
                 [["major", "category", "subcategory"]],
                 updatesubcategoryFormBoptionssubcategories
                );
   activateTHISForm("subcategorydeletebutton", 
                 "/courses/deletesubcategory",
                 null,
                 null,
                 ["subcategoryFormBoptionssubcategories"],
                 [["major", "category", "subcategory"]],
                 updatesubcategoryFormBoptionssubcategories
                );
}
function updaterequirementFormAoptionssubcategories(){
   let subcategories_data = getSessionData("subcategory");
   let subcategories:string[] = [];
   for (const subcategory of subcategories_data) {
     subcategories.push(subcategory[0]);
   }
   addSelectionOptions("requirementFormAoptionssubcategories", subcategories);
} 
function activateRequirementFormA(){
   activateTHISForm("requirementaddbutton", 
                 "/courses/createrequirement",
                 ["requirementFormArequirement", "requirementFormAcredit"],
                 ["requirement", "credit"],
                 ["requirementFormAoptionssubcategories"],
                 [["major", "category", "subcategory"]],
                 updaterequirementFormAoptionssubcategories 
                );
}
function updaterequirementFormBoptionsrequirements() {
   let requirements_data = getSessionData("requirement");
   let requirements:string[] = [];
   for (const requirement of requirements_data) {
      requirements.push(requirement[0]);
   }
   addSelectionOptions("requirementFormBoptionsrequirements", requirements);
}
function activateRequirementFormB(){
   updaterequirementFormBoptionsrequirements(); 
   activateTHISForm("requirementaddbutton", 
                 "/courses/createrequirement",
                 null,
                 null,
                 ["requirementFormBoptionsrequirements"],
                 [["major", "category", "subcategory", "requirement"]],
                 updaterequirementFormBoptionsrequirements
                );
    activateTHISForm("requirementdeletebutton", 
                 "/courses/deleterequirement",
                 null,
                 null,
                 ["requirementFormBoptionsrequirements"],
                 [["major", "category", "subcategory", "requirement"]],
                 updaterequirementFormBoptionsrequirements
                );
}
function updatecourseFormAoptionsrequirements() {
   let requirements_data = getSessionData("requirement");
   let requirements:string[] = [];
   for (const requirement of requirements_data) {
      requirements.push(requirement[0]);
   }
   addSelectionOptions("courseFormAoptionsrequirements", requirements); 
}
function activateCourseFormA(){
   updatecourseFormAoptionsrequirements();
   activateTHISForm("coursecreatebutton", 
                 "/courses/createcourse",
                 ["courseFormAcourse", "courseFormAcredit"],
                 ["course", "credit"],
                 ["courseFormAoptionsrequirements"],
                 [["major", "category", "subcategory", "requirement"]],
                 updatecourseFormAoptionsrequirements
                );
}
function updatecourseFormBoptionscourses() {
   let courses_data = getSessionData("course");
   let courses:string[] = [];
   for (const course of courses_data) {
     courses.push(course[0]);
   }
   addSelectionOptions("courseFormBoptionscourses", courses);
}
function activateCourseFormB(){
   updatecourseFormBoptionscourses();
   activateTHISForm("courseaddbutton", 
                 "/courses/createcourse",
                 null,
                 null,
                 ["courseFormBoptionscourses"],
                 [["major", "category", "subcategory", "requirement", "course" ]],
                 updatecourseFormBoptionscourses
                );
   activateTHISForm("coursedeletebutton", 
                 "/courses/deletecourse",
                 null,
                 null,
                 ["courseFormBoptionscourses"],
                 [["major", "category", "subcategory", "requirement", "course" ]],
                 updatecourseFormBoptionscourses
                );
}
function updateprereqFormAoptions(){
   let courses_data = getSessionData("course");
   let courses:string[] = [];
   for (const course of courses_data) {
      courses.push(course[0]);
   }
   addSelectionOptions("prereqFormAoptionscourses", courses);
   addSelectionOptions("prereqFormAoptionsprereqs", courses);
}
function activatePrereqForms() {
    updateprereqFormAoptions();
    // cant be the same course
    activateTHISForm("prereqaddbutton", 
                 "/courses/createprereq",
                 null,
                 null,
                 ["prereqFormAoptionscourses", "prereqFormAoptionsprereqs"],
                 [["major", "category", "subcategory", "requirement", "course"],
                   ["pmajor", "pcategory", "psubcategory", "prequirement", "pcourse"]],
                 updateprereqFormAoptions 
                );
    activateTHISForm("prereqdeletebutton", 
                 "/courses/deleteprereq",
                 null,
                 null,
                 ["prereqFormAoptionscourses", "prereqFormAoptionsprereqs"],
                 [["major", "category", "subcategory", "requirement", "course"],
                   ["pmajor", "pcategory", "psubcategory", "prequirement", "pcourse"]],
                  updateprereqFormAoptions
                );
}
function updateapFormAoptionscourses() {
   let courses_data = getSessionData("course");
   let courses:string[] = [];
   for (const course of courses_data) {
      courses.push(course[0]);
   };
   addSelectionOptions("apFormAoptionscourses", courses);
}
function activateAPFormA(){
   updateapFormAoptionscourses();
   activateTHISForm("apcreatebutton", 
                 "/courses/createap",
                 ["apFormAtest", "apFormAmin", "apFormAmax"],
                 ["test", "scoremin", "scoremax"],
                 ["apFormAoptionscourses"],
                 [["major", "category", "subcategory", "requirement", "course"]],
                 updateapFormAoptionscourses
                );
}
function updateapFormBoptions() {
   let courses_data = getSessionData("course");
   let courses:string[] = [];
   for (const course of courses_data) {
      courses.push(course[0]);
   }
   addSelectionOptions("apFormBoptionscourses", courses);
   let tests = getSessionData("test");
   addSelectionOptions("apFormBoptionstests", tests);
}
function activateAPFormB(){
    updateapFormBoptions();
    activateTHISForm("apaddbutton", 
                 "/courses/createap",
                 null,
                 null,
                 ["apFormBoptionstests", "apFormBoptionscourses"],
                 [["test", "scoremin", "scoremax"],
                   ["major", "category", "subcategory", "requirement", "course"]],
                   updateapFormBoptions
                );
    activateTHISForm("apdeletebutton", 
                 "/courses/deleteap",
                 null,
                 null,
                 ["apFormBoptionstests", "apFormBoptionscourses"],
                 [["test", "scoremin", "scoremax"],
                   ["major", "category", "subcategory", "requirement", "course"]],
                   updateapFormBoptions
                );
}



