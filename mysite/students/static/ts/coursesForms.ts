/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />
/// <reference path="ajaxForm.ts" />

// major create
function activateMajorFormA(){
   activateTHISForm("majorcreatebutton", "/courses/createmajor", 
      ["majorFormAmajor"], ["major"],
      null, null,
      null
      ); 
}
// major delete
function updatemajorFormBoptionsmajors() {
   addSelectionOptions("majorFormBoptionsmajors", getSessionData("major"));
}
function activateMajorFormB(){
   updatemajorFormBoptionsmajors();
   activateTHISForm("majordeletebutton", "/courses/deletemajor",
      null, null,
      ["majorFormBoptionsmajors"], 
      [["major"]],
      updatemajorFormBoptionsmajors
   );
}
//------------------------------
// category create
function updatecategoryFormAoptionsmajors(){
   addSelectionOptions("categoryFormAoptionsmajors", getSessionData("major"));
}
function activateCategoryFormA(){
   updatecategoryFormAoptionsmajors();
   activateTHISForm("categorycreatebutton", "/courses/createcategory",
      ["categoryFormAcategory"], ["category"],
      ["categoryFormAoptionsmajors"], 
      [["major"]],
      updatecategoryFormAoptionsmajors
      );
}
// category delete
function updatecategoryFormBoptionscategories(){
   addSelectionOptions("categoryFormBoptionscategories", getSessionData("category"));
}
function activateCategoryFormB(){
   updatecategoryFormBoptionscategories();
   activateTHISForm("categorydeletebutton", "/courses/deletecategory",
      null, null,
      ["categoryFormBoptionscategories"], 
      [["major", "category"]],
      updatecategoryFormBoptionscategories
      );
}
// category add
function updatecategoryFormCoptionscategories(){
   addSelectionOptions("categoryFormCoptionsmajors", getSessionData("major"));
   addSelectionOptions("categoryFormCoptionscategories", getSessionData("category"));
}
function activateCategoryFormC(){
   updatecategoryFormCoptionscategories(); 
   activateTHISForm("categoryaddbutton", "/courses/createcategory",
      null, null,
      ["categoryFormCoptionscategories", "categoryFormCoptionsmajors"], 
      [["major", "category"], ["major"]],
      updatecategoryFormCoptionscategories
   );
}
//------------------------------
// subcategory create
function updatesubcategoryFormAoptionscategories(){
   addSelectionOptions("subcategoryFormAoptionscategories", getSessionData("category"));
}
function activateSubcategoryFormA(){
   updatesubcategoryFormAoptionscategories();
   activateTHISForm("subcategorycreatebutton", "/courses/createsubcategory",
      ["subcategoryFormAsubcategory", "subcategoryFormAnote"], ["subcategory", "note"],
      ["subcategoryFormAoptionscategories"], 
      [["major", "category"]],
      updatesubcategoryFormAoptionscategories
   );
}
// subcategory delete
function updatesubcategoryFormBoptionssubcategories(){
   addSelectionOptions("subcategoryFormBoptionssubcategories", getSubSessionData("subcategory"));
}
function activateSubcategoryFormB() {
   updatesubcategoryFormBoptionssubcategories();
   activateTHISForm("subcategorydeletebutton", "/courses/deletesubcategory",
      null, null,
      ["subcategoryFormBoptionssubcategories"], 
      [["major", "category", "subcategory"]],
      updatesubcategoryFormBoptionssubcategories
      );
}
// subcategory add
function updatesubcategoryFormCoptionssubcategories(){
   addSelectionOptions("subcategoryFormCoptionscategories", getSessionData("category"));
   addSelectionOptions("subcategoryFormCoptionssubcategories", getSubSessionData("subcategory"));
}
function activateSubcategoryFormC(){
   updatesubcategoryFormCoptionssubcategories();
   activateTHISForm("subcategoryaddbutton", "/courses/createsubcategory",
      null, null,
      ["subcategoryFormCoptionssubcategories", "subcategoryFormCoptionscategories"], 
      [["major", "category", "subcategory"], ["major", "category"]],
      updatesubcategoryFormCoptionssubcategories
      );
}
//------------------------------
// requirement create
function updaterequirementFormAoptionssubcategories(){
   addSelectionOptions("requirementFormAoptionssubcategories", getSubSessionData("subcategory"));
} 
function activateRequirementFormA(){
   updaterequirementFormAoptionssubcategories(); 
   activateTHISForm("requirementaddbutton",  "/courses/createrequirement",
      ["requirementFormArequirement", "requirementFormAcredit"], ["requirement", "credit"],
      ["requirementFormAoptionssubcategories"], 
      [["major", "category", "subcategory"]],
      updaterequirementFormAoptionssubcategories 
      );
}
// requirement delete
function updaterequirementFormBoptionsrequirements() {
   addSelectionOptions("requirementFormBoptionsrequirements", getSubSessionData("requirement"));
}
function activateRequirementFormB(){
   updaterequirementFormBoptionsrequirements(); 
   activateTHISForm("requirementdeletebutton", "/courses/deleterequirement",
      null, null,
      ["requirementFormBoptionsrequirements"], 
      [["major", "category", "subcategory", "requirement"]],
      updaterequirementFormBoptionsrequirements
      );
}
// requirement add
function updaterequirementFormCoptionsrequirements() {
   addSelectionOptions("requirementFormCoptionssubcategories", getSubSessionData("subcategory")); 
   addSelectionOptions("requirementFormCoptionsrequirements", getSubSessionData("requirement"));
}
function activateRequirementFormC(){ 
   updaterequirementFormCoptionsrequirements();
   activateTHISForm("requirementaddbutton",  "/courses/createrequirement",
      null, null,
      ["requirementFormBoptionsrequirements","requirementFormCoptionssubcategories"], 
      [["major", "category", "subcategory", "requirement"], ["major", "category", "subcategory"]],
      updaterequirementFormCoptionsrequirements
      );
}
//------------------------------
// course create
function updatecourseFormAoptionsrequirements() {
   addSelectionOptions("courseFormAoptionsrequirements", getSubSessionData("requirement")); 
}
function activateCourseFormA(){
   updatecourseFormAoptionsrequirements();
   activateTHISForm("coursecreatebutton", "/courses/createcourse",
      ["courseFormAcourse", "courseFormAcredit"], ["course", "credit"],
      ["courseFormAoptionsrequirements"], 
      [["major", "category", "subcategory", "requirement"]],
      updatecourseFormAoptionsrequirements
      );
}
// course delete
function updatecourseFormBoptionscourses() {
   addSelectionOptions("courseFormBoptionscourses", getSubSessionData("course")); 
}
function activateCourseFormB(){
   updatecourseFormBoptionscourses();
   activateTHISForm("courseaddbutton", "/courses/createcourse",
      null, null,
      ["courseFormBoptionscourses"],
      [["major", "category", "subcategory", "requirement", "course" ]],
      updatecourseFormBoptionscourses
      );
}
// course add
function updatecourseFormCoptionscourses() {
   addSelectionOptions("courseFormCoptionscourses", getSubSessionData("course")); 
   addSelectionOptions("courseFormCoptionsrequirements", getSubSessionData("requirement"));
}
function activateCourseFormC(){
   activateTHISForm("coursedeletebutton", "/courses/deletecourse",
      null, null,
      ["courseFormCoptionscourses","courseFormCoptionsrequirements"], 
      [["major", "category", "subcategory", "requirement", "course" ],["major", "category", "subcategory", "requirement"]],
      updatecourseFormBoptionscourses
      );
}
//------------------------------
// prereq add and delete
function updateprereqForms(){
   addSelectionOptions("prereqFormAoptionscourses", getSubSessionData("course"));
   addSelectionOptions("prereqFormAoptionsprereqs", getSubSessionData("course"));
}
function activatePrereqForms() {
   updateprereqForms();
   // cant be the same course
   activateTHISForm("prereqaddbutton", "/courses/createprereq",
      null, null,
      ["prereqFormAoptionscourses", "prereqFormAoptionsprereqs"], 
      [["major", "category", "subcategory", "requirement", "course"],["pmajor", "pcategory", "psubcategory", "prequirement", "pcourse"]],
      updateprereqForms
      );
   activateTHISForm("prereqdeletebutton", "/courses/createprereq",
      null, null,
      ["prereqFormAoptionscourses", "prereqFormAoptionsprereqs"], 
      [["major", "category", "subcategory", "requirement", "course"], ["pmajor", "pcategory", "psubcategory", "prequirement", "pcourse"]],
      updateprereqForms
      );
}
//------------------------------
// ap create
function updateapFormAoptionscourses() {
   addSelectionOptions("apFormAoptionscourses", getSubSessionData("course"));
}
function activateAPFormA(){
   updateapFormAoptionscourses();
   activateTHISForm("apcreatebutton", "/courses/createap",
      ["apFormAtest", "apFormAmin", "apFormAmax"], ["test", "scoremin", "scoremax"],
      ["apFormAoptionscourses"], 
      [["major", "category", "subcategory", "requirement", "course"]],
      updateapFormAoptionscourses
      );
}
function updateapFormBoptions() {
   addSelectionOptions("apFormBoptionscourses", getSubSessionData("course"));
   addSelectionOptions("apFormBoptionstests", getSessionData("test")); 
}
function activateAPFormB(){
   updateapFormBoptions();
   activateTHISForm("apaddbutton", "/courses/createap",
      null, null,
      ["apFormBoptionstests", "apFormBoptionscourses"], 
      [["test", "scoremin", "scoremax"], ["major", "category", "subcategory", "requirement", "course"]],
      updateapFormBoptions
   );
   activateTHISForm("apdeletebutton", "/courses/deleteap",
      null, null,
      ["apFormBoptionstests", "apFormBoptionscourses"],
      [["test", "scoremin", "scoremax"], ["major", "category", "subcategory", "requirement", "course"]],
      updateapFormBoptions
      );
}



