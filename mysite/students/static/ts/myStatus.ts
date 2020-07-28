/// <reference path="helperForms.ts" />
/// <reference path="dataTree.ts" />

function getMyCourses(){
  let output:string[] = [];
  let cd_courses = getSessionData("mycourse");
  if(cd_courses == null){ return output;}
  let tests = getSessionData("myap");
  if(tests == null){ return output;}
    for (const test of tests) {
      let name = `mycourseap-${test.substring(0, test.indexOf("/"))}`;
      let tranfer = getSessionData(name)
      if(tranfer != null){
        for (const course of tranfer) {
          output.push(`before/${course}`);
        }
      }
    }
  for (const course of cd_courses) {
    output.push(course);
  }
  return output;
}

function recordCompletion(
  session_data_list:any[], 
  child_session_data_list:any[], 
  child_completion_list:string[],
  ){
  let output_completed_list:string[] = [];
  if(session_data_list==null){return output_completed_list;}
  for (const data_instance of session_data_list){
    let data_relation = data_instance;
    let data_child_requirements = [];
    if (child_session_data_list == null){ return output_completed_list;}
    for (const child_instance of child_session_data_list) {
      let child_relation = child_instance;
      if (child_relation.indexOf(data_relation)!=-1){
        data_child_requirements.push(child_relation);
      } // gather requirements for this data instance
    }
    if (child_completion_list == null){ return output_completed_list;}
    for (const child of child_completion_list) {
      let name = child.substring(child.lastIndexOf("/")+1);
      let to_delete = []
      for (let index = data_child_requirements.length-1; index>=0 ; index--) {
        const element = data_child_requirements[index];
        let test = element.substring(element.lastIndexOf("/")+1);
        if(test == name){
          to_delete.push(index);
        }
      }
      let temp = [];
      for (let index = 0; index < data_child_requirements.length; index++) {
        if(!inarray(to_delete, index)){ temp.push(data_child_requirements[index]);}
      }
      data_child_requirements = temp;
    } // remove completed requirements from list
    if(data_child_requirements.length==0){
      output_completed_list.push(data_relation);
    }
  }
  return output_completed_list;
}

function buildStatusTree(){
  // list of completed courses
  let cd_courses = getMyCourses();
  let courses = getSubSessionData("course");
  // console.log("----------cour")
  // console.log(cd_courses)
  // console.log(courses)
  // list of completed requirements
  let cd_requirements = [];
  let requirements = getSubSessionData("requirement");
  cd_requirements = recordCompletion(requirements, courses, cd_courses);
  // console.log("----------req")
  // console.log(cd_requirements)
  // console.log(requirements)
  // list of completed subcategories
  let cd_subcategories = [];
  let subcategories = getSubSessionData("subcategory");
  cd_subcategories = recordCompletion(subcategories, requirements, cd_requirements);
  // console.log("----------sub")
  // console.log(cd_subcategories)
  // console.log(subcategories)
  // list of completed categories
  let cd_categories = [];
  let categories = getSessionData("category");
  cd_categories = recordCompletion(categories, subcategories, cd_subcategories);
  // console.log("----------cat")
  // console.log(cd_categories)
  // console.log(categories)
  // list of completed majors
  let cd_majors:string[]  = [];
  let majors = getSessionData("major");
  cd_majors = recordCompletion(majors, categories, cd_categories);
  // console.log("----------major")
  // console.log(cd_majors)
  // console.log((majors))
  // build data tree with completion marks
  let order = ["MAJ","CAT","SUB","REQ","COU"]
  let workspace_id = "mystatusdata";
  clearData(workspace_id);
  function build(cd_list:string[], data_list:any[], iscourses:boolean){
    for (const data_instance of data_list) {
      if(data_instance != null){
        let relation_list = readMySessionString(data_instance);
        if (relation_list.length == 1) { 
          if(inarray(cd_majors, data_instance)){ addStatusList(workspace_id, `MAJ:${data_instance}`, true);
          } else { addStatusList(workspace_id, `MAJ:${data_instance}`, false);
          }
        } else {
          let leparent = "";
          let lechild = "";
          let name = "";
          for (let index = 0; index < relation_list.length; index++) {
            name = `${name}${order[index]}:${relation_list[index]}`;
            if(index == relation_list.length - 2){ leparent = name; }
            if(index == relation_list.length - 1){ lechild = name; }
          }
          
          if(iscourses){
            let lename = data_instance.substring(data_instance.lastIndexOf("/")+1);
            if(inarray(cd_list, lename)){ addStatusList(leparent, lechild, true);
            } else { addStatusList(leparent, lechild, false);}
          } else {

            if(inarray(cd_list, data_instance)){ addStatusList(leparent, lechild, true);
            } else { addStatusList(leparent, lechild, false);}

          }

        }
      } 
    }
  }
  build(cd_majors, majors, false);
  build(cd_categories, categories, false);
  build(cd_subcategories, subcategories, false);
  build(cd_requirements, requirements, false);
  let names = [];
    for (const name of getMyCourses()) {
      names.push( name.substring(name.indexOf("/")+1) );
    }
  build(names, courses, true);
  cleanUPStatus();
}


function cleanUPStatus(){
  let workspace_id = "mystatusdata";
  let order = ["MAJ","CAT","SUB","REQ","COU"]
  let tags = document.getElementById(workspace_id).getElementsByTagName("span");
  for (const tag of tags) {
    let id = tag.id;
    let list_id = id.substring(id.indexOf("-")+1);
    let important = id.substring(indexoflasttag(id, order));
    let list = document.getElementById(list_id);
   
    if (list.children.length > 0){
      let check_list = [];
      for (const child of list.children) {
        for(const item of child.children){
          if(item.id.indexOf("symbol")!=-1){
            if(item.className.indexOf("checkmark")!=-1){
              check_list.push(0);
            } else { check_list.push(1);}
          }
        }
      }
      let check = 0;
      for (const num of check_list) {check = check + num;}
      if (check == 0){
        document.getElementById(id).className = "checkmark";
      } else { document.getElementById(id).className = "xmark";}
      
    }

    if (list.children.length == 0 && important.indexOf("COU")==-1){
      document.getElementById(id).className = "checkmark";
    }

    document.getElementById(id).innerHTML = important; 
  }
}



function indexoflasttag(input:string, tags:string[]){
  let data:{[input:string]:number;} = {};
  for (const tag of tags) {
    data[tag] = input.lastIndexOf(tag);
  }
  let last = -1;
  for (const tag of tags) {
    if(data[tag] > last){ last = data[tag]}
  }
  return last;
}
