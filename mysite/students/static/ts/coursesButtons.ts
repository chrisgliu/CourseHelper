/// <reference path='toggle.ts'/>
/// <reference path='coursesData.ts' />

let forms = ['majorforms', 'categoryforms', 'subcategoryforms',
      'requirementforms', 'courseforms', 'prereqforms', 'apforms'];
//some button functions for toggling
function activateCourseButtons(){
    let refresh = document.getElementById('refreshcoursesdata')
    // refresh button is shown only when user is signed in
    if (refresh != null) {
      refresh.onclick = ()=>{ 
        updateCoursesData();
      }  
      document.getElementById('majoroperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('majorforms');
        activateMajorFormA();
        activateMajorFormB();
      }
      document.getElementById('categoryoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('categoryforms');
        activateCategoryFormA();
        activateCategoryFormB();
      }
      document.getElementById('subcategoryoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('subcategoryforms');
        activateSubcategoryFormA();
        activateSubcategoryFormB();
      }
      document.getElementById('requirementoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('requirementforms');
        activateRequirementFormA();
        activateRequirementFormB();
      }
      document.getElementById('courseoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('courseforms');
        activateCourseFormA();
        activateCourseFormB();
      }
      document.getElementById('prereqoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('prereqforms');
        activatePrereqForms();
      }
      document.getElementById('apoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('apforms');
        activateAPFormA();
        activateAPFormB();
      }
    }
    let operations = [
      "majorFormA", "majorFormB",
      "categoryFormA", "categoryFormB",
      "subcategoryFormA", "subcategoryFormB",
      "requirementFormA", "requirementFormB",
      "courseFormA", "courseFormB",
      "prereqFormA", "apFormA", "apFormB"
    ];
    if (document.getElementById('majorforms') != null) {
      document.getElementById('createmajoroperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("majorFormA");
      }
      document.getElementById('deletemajoroperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("majorFormB"); 
      }
    }
    if (document.getElementById('categoryforms') != null) {
      document.getElementById('createcategoryoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("categoryFormA");
      }
      document.getElementById('addcategoryoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("categoryFormB"); 
        showIt("categoryaddbutton");
        dontShowIt("categorydeletebutton");
      }
      document.getElementById('deletecategoryoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("categoryFormB"); 
        showIt("categorydeletebutton");
        dontShowIt("categoryaddbutton")
      }
    }
    if (document.getElementById('subcategoryforms') != null) {
      document.getElementById('createsubcategoryoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("subcategoryFormA");
      }
      document.getElementById('addsubcategoryoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("subcategoryFormB"); 
        showIt("subcategoryaddbutton");
        dontShowIt("subcategorydeletebutton"); 
      }
      document.getElementById('deletesubcategoryoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("subcategoryFormB");
        showIt("subcategorydeletebutton");
        dontShowIt("subcategoryaddbutton"); 
      }
    }
    if (document.getElementById('requirementforms') != null) {
      document.getElementById('createrequirementoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("requirementFormA");
      }
      document.getElementById('addrequirementoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("requirementFormB");
        showIt("requirementdeletebutton");
        dontShowIt("requirementaddbutton");  
      }
      document.getElementById('deleterequirementoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("requirementFormB"); 
        showIt("requirementdeletebutton");
        dontShowIt("requirementaddbutton"); 
      }
    }
    if (document.getElementById('courseforms') != null) {
      document.getElementById('createcourseoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("courseFormA");
      }
      document.getElementById('addcourseoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("courseFormB"); 
        showIt("coursedeletebutton");
        dontShowIt("coursetaddbutton"); 
      }
      document.getElementById('deletecourseoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("courseFormB"); 
        showIt("courseaddbutton"); 
        dontShowIt("coursedeletebutton");
      }
    } 
    if (document.getElementById('prereqforms') != null) {
      document.getElementById('addprereqoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("prereqFormA"); 
        showIt("prereqaddbutton");
        dontShowIt("prereqdeletebutton");
      }
      document.getElementById('deleteprereqoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("prereqFormA");
        showIt("prereqdeletebutton");
        dontShowIt("prereqaddbutton");
      }
    } 
    if (document.getElementById('apforms') != null) {
      document.getElementById('createapoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("apFormA");
      }
      document.getElementById('addapoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("apFormB"); 
        showIt("apaddbutton");
        dontShowIt("apdeletebutton");
      }
      document.getElementById('deleteapoperation').onclick = () => {
        for (const operation of operations) { dontShowIt(operation); } 
        showIt("apFormB"); 
        showIt("apdeletebutton");
        dontShowIt("apaddbutton");
      }
    } 
}
