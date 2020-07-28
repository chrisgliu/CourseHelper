/// <reference path='toggle.ts'/>
/// <reference path='helperData.ts' />
/// <reference path="myMajors.ts" />
/// <reference path="myAP.ts" />
/// <reference path="myYears.ts" />
/// <reference path="betterDark.ts" />
/// <reference path="helperForms.ts" />
/// <reference path="myStatus.ts" />



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
        showTranferCourses("test");
        activateHelperForms();
        buildStatusTree();
      }
    }
    document.getElementById("aptoggle").onclick = ()=> {
      toggleShow("myapactions");
      showAPTransfer();
      document.getElementById("aptoggle").classList.toggle("caret-down");
    }
    document.getElementById("extratermbutton").onclick = ()=> {
      toggleShow("mytermactions");
    }
    document.getElementById("extrayearbutton").onclick = ()=> {
      toggleShow("tranfercredit");
    }
    document.getElementById('mymajorbutton').onclick = ()=>{
        toggleShow("status");
//      toggleShow('mymajoractions');
//      showTrackedMajors();
//      activateMajorManagerAdd();
//      activateMajorManagerDelete();
    }
    
    document.getElementById('mycoursesbutton').onclick = ()=>{
      toggleShow('mycourseoperation');
      let year = getLatestYearID();
      let termlist = (<HTMLUListElement> document.getElementById(year));
      let header = termlist.getElementsByTagName("span");
      let terms:string[] = [];
      let term_in_question:string = "";
      for (const element of header) {
        let id = element.id;
        if (id.indexOf("TERM")!=-1){ terms.push(id);}
      }
      term_in_question = terms[terms.length-1];
      for (const term_id of terms) {
        let symbol = document.getElementById(term_id);
            if (symbol.className == "caret caret-down"){
                term_in_question = term_id;
            }
      }
      let term_name = term_in_question.substring(term_in_question.indexOf("-")+1);
      showTermCourses(term_name);
      document.getElementById("thistermname").innerHTML = term_name;
      activateCourseManagerAdd();
      activateCourseManagerDelete();
    }
    document.getElementById('myapbutton').onclick = ()=>{
      toggleShow('mytestoperation');
      activateTestManagerAdd();
      activateTestManagerDelete();
    } 
}
 
