///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
// courses tree data

//Major:test
function addCoursesData(workspace_id:string, response:Document){
  let majors = response.getElementsByTagName('major');
  for (const major of majors) {
    let major_name = major.getElementsByTagName('major_name')[0].innerHTML;
    addDataList(workspace_id, `Major:${major_name}`);
    let major_categories = major.getElementsByTagName('categories')[0];
    let categories = major_categories.getElementsByTagName('category');
    for (const category of categories) {
      let category_name = category.getElementsByTagName('category_name')[0].innerHTML;  
      addDataList(`Major:${major_name}`, `Category:${category_name}`);
      let category_subcategories = category.getElementsByTagName('subcategories')[0];
      let subcategories = category_subcategories.getElementsByTagName('subcategory');
      for (const subcategory of subcategories) {
        let subcategory_name = subcategory.getElementsByTagName('subcategory_name')[0].innerHTML;  
        addDataList(`Category:${category_name}`, `Subcategory:${subcategory_name}`);
        let subcategory_note = subcategory.getElementsByTagName('subcategory_data')[0].innerHTML;
        addSpecificData(`Subcategory:${subcategory_name}`, subcategory_note);
        let subcategory_requirements = subcategory.getElementsByTagName('requirements')[0];
        let requirements = subcategory_requirements.getElementsByTagName('requirement');
        for (const requirement of requirements) {
          let requirement_name = requirement.getElementsByTagName('requirement_name')[0].innerHTML;
          addDataList(`Subcategory:${subcategory_name}`, `Requirement:${requirement_name}`);
          let requirement_credit = requirement.getElementsByTagName('requirement_data')[0].innerHTML;
          addSpecificData(`Requirement:${requirement_name}`, requirement_credit);
          let requirement_courses = requirement.getElementsByTagName('courses')[0];
          let courses = requirement_courses.getElementsByTagName('course');
          for (const course of courses) {
            let course_name = course.getElementsByTagName('course_name')[0].innerHTML;
            addDataList(`Requirement:${requirement_name}`, `Course:${course_name}`);
            let course_credit = course.getElementsByTagName('course_data')[0].innerHTML;
            addSpecificData(`Course:${course_name}`, course_credit);
            let course_prereqs = course.getElementsByTagName('prereqs')[0];
            if (course_prereqs != null) {
              addDataList(`Course:${course_name}`, `Prereq:${course_name}`);
              let prereqs = course_prereqs.getElementsByTagName('prereq');
              for (const prereq of prereqs) {
                let prereq_name = prereq.getElementsByTagName('prereq_name')[0].innerHTML;
                addSpecificData(`Prereq:${course_name}`, prereq_name)
              }
            }
            let course_ap = course.getElementsByTagName('ap')[0];
            if (course_ap != null) {
              addDataList(`Course:${course_name}`, `Ap:${course_name}`);
              let tests = course_ap.getElementsByTagName('test');
              for (const test of tests) {
                let test_name = test.getElementsByTagName('test_name')[0].innerHTML;
                addSpecificData(`Ap:${course_name}`, test_name);
              }   
            }
          }
        }  
      }
    }
  }
}

function updateCoursesData(){
  let workspace_id = 'coursesdata';
  clearData(workspace_id);
  let url_source = '/requestcoursesdata';
  requestAJAX(url_source, workspace_id, addCoursesData);
}





















