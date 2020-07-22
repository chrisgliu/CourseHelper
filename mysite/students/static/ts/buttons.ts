/// <reference path='toggle.ts'/>
/// <reference path="coursesdata.ts" />
/// <reference path="helperdata.ts" />


//some button functions for toggling
function activateCourseButtons(){
    let forms = ['majorforms', 'categoryforms', 'subcategoryforms',
      'requirementforms', 'courseforms', 'prereqforms', 'apforms'];
    let refresh = document.getElementById('refreshcoursesdata')
    // refresh button is shown only when user is signed in
    if (refresh != null) {
      refresh.onclick = ()=>{ updateCoursesData();}  
      document.getElementById('majoroperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('majorforms');
      }
      document.getElementById('categoryoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('categoryforms');
      }
      document.getElementById('subcategoryoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('subcategoryforms');
      }
      document.getElementById('requirementoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('requirementforms');
      }
      document.getElementById('courseoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('courseforms');
      }
      document.getElementById('prereqoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('prereqforms');
      }
      document.getElementById('apoperation').onclick = ()=>{
        for (const item of forms) { dontShowIt(item);}
        showIt('apforms');
      }
    }
  }
  
function activateHelperButtons() {
    let actions  = ['mymajoractions', 'mytermactions', 'myapactions',
    'tranfercredit', 'status',
    'mycourseoperation'] 

    let update = document.getElementById('updatehelperdata')
    // update button is shown only when user is signed in
    if (update != null) {
      update.onclick = ()=>{ 
        updateMajorData();
        updateAPData();
        updatePlannerData();
        updateScheduleData();
      }
    }
     
    document.getElementById('mymajorbutton').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('mymajoractions');
    }

    //testing
    document.getElementById('testbuttonterm').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('mytermactions');
    }
    document.getElementById('testbuttonap').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('myapactions');
    }
    document.getElementById('testbuttontranfer').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('tranfercredit');
    }
    document.getElementById('testbuttonstatus').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('status');
    }
    ///testing
    
    document.getElementById('mycoursesbutton').onclick = ()=>{
      showIt('mycourseoperation');
    }
    document.getElementById('myapbutton').onclick = ()=>{
      showIt('mytestoperation');
    } 
}
 
