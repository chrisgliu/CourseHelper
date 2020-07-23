/// <reference path='toggle.ts'/>
/// <reference path='helperData.ts' />
/// <reference path="myMajors.ts" />
/// <reference path="myAP.ts" />



let actions  = ['mymajoractions', 'mytermactions', 'myapactions',
    'tranfercredit', 'status',
    'mycourseoperation'] 

function activateHelperButtons() {
    let update = document.getElementById('updatehelperdata')
    // update button is shown only when user is signed in
    if (update != null) {
      update.onclick = ()=>{ 
        updateMajorData();
        updateAPData();
        updatePlannerData();
        updateScheduleData();
        showTrackedMajors();
        showAPTransfer();
      }
    }
     
    document.getElementById('mymajorbutton').onclick = ()=>{
      toggleShow('mymajoractions');
      showTrackedMajors();
    }
    
    document.getElementById('mycoursesbutton').onclick = ()=>{
      toggleShow('mycourseoperation');
    }
    document.getElementById('myapbutton').onclick = ()=>{
      toggleShow('mytestoperation');
    } 
}
 
