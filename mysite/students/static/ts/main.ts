/// <reference path='toggle.ts'/>
/// <reference path="coursesdata.ts" />


document.addEventListener("DOMContentLoaded", () => {
// displaying tree data 
  let treedata = document.getElementsByClassName("caret");
  for (const toggle of treedata) {
    toggle.addEventListener("click", function(){
      let data: HTMLElement = toggle.parentElement.querySelector(".nested")
	    toggleIt(data)
      toggle.classList.toggle("caret-down");
    });
  }
// nav buttons
  document.getElementById('creditsneeded').onclick = ()=>{
    showIt('section-b')
	  dontShowIt('section-a')
    dontShowIt('section-c') 
  }
  document.getElementById('creditswanted').onclick = () =>{
	  showIt('section-c')
	  dontShowIt('section-a')
	  dontShowIt('section-b')
  }
  let signin = document.getElementById('signin')
  if (signin != null) {
    signin.onclick = ()=>{ showIt('signinform') }
  }
  let signup = document.getElementById('signup')
  if (signup != null) {
    signup.onclick = ()=>{ showIt('signupform') }
  }
  let signout = document.getElementById('signout')
  if (signout != null) {
    signout.onclick = ()=>{ window.location.href = '/signOut' }
  }
  document.getElementById('cancelsignin').onclick = ()=>{
    dontShowIt('signinform')
  }
  document.getElementById('cancelsignup').onclick = ()=>{
  	dontShowIt('signupform')
  }
// course buttons
  let forms = ['majorforms', 'categoryforms', 'subcategoryforms',
    'requirementforms', 'courseforms', 'prereqforms', 'apforms'];

  document.getElementById('refreshcoursesdata').onclick = ()=>{
    updateCoursesData(); 
  }
  document.getElementById('majoroperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('majorforms');
  }
  document.getElementById('categoryoperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('categoryforms');
  }
  document.getElementById('subcategoryoperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('subcategoryforms');
  }
  document.getElementById('requirementoperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('requirementforms');
  }
  document.getElementById('courseoperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('courseforms');
  }
  document.getElementById('prereqoperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('prereqforms');
  }
  document.getElementById('apoperation').onclick = ()=>{
    for (const item of forms) {
      dontShowIt(item);
    }
    showIt('apforms');
  }
});



