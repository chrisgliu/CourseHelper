/// <reference path='toggle.ts'/>
/// <reference path='coursesDataTree.ts' />
/// <reference path='helperData.ts' />
/// <reference path='coursesButtons.ts' />
/// <reference path='helperButtons.ts' />
/// <reference path='betterDark.ts' />


document.addEventListener("DOMContentLoaded", () => {
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
  activateCourseButtons();
  // helper buttons
  activateHelperButtons();

  document.getElementById("darkmode").onclick = ()=> {
    darkmode();
  }
});



