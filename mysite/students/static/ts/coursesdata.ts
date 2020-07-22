///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
///<reference path='sessiondata.ts'/>
// courses tree data

function readMajors(majors:HTMLCollection) {
  let major_data = [];
  for (const major of majors) {
    let major_content = major.childNodes;
    let major_name = ''; 
    let categories_node = null;
    for (const node of major_content) {
      if (node.nodeName == 'major_name') { major_name = node.textContent;}
      if (node.nodeName == 'categories' && node.hasChildNodes()) { categories_node = node;}
    }
    let data = {'major_name':major_name, 'categories':categories_node};
    major_data.push(data);
  }
  return major_data;
}
function readCategories(categories:NodeList) {
  let category_data = [];
  for (const category of categories) {
    let category_content = category.childNodes;
    let category_name = '';
    let subcategories_node = null;
    for (const node of category_content) {
      if (node.nodeName == 'category_name') { category_name = node.textContent;}
      if (node.nodeName == 'subcategories' && node.hasChildNodes()) { subcategories_node = node;}
    }
    let data = {'category_name':category_name, 'subcategories':subcategories_node};
    category_data.push(data);
  }
  return category_data;
}
function readSubcategories(subcategories:NodeList) {
  let subcategory_data = [];
  for (const subcategory of subcategories) {
    let subcategory_content = subcategory.childNodes;
    let subcategory_name = '';
    let requirements_node = null;
    for (const node of subcategory_content) {
      if (node.nodeName == 'subcategory_name') { subcategory_name = node.textContent;}
      if (node.nodeName == 'requirements' && node.hasChildNodes()) { requirements_node = node;}
    }
    let data = {'subcategory_name':subcategory_name, 'requirements':requirements_node};
    subcategory_data.push(data);
  }
  return subcategory_data;
}
function readRequirements(requirements:NodeList) {
  let requirement_data = [];
  for (const requirement of requirements) {
    let requirement_content = requirement.childNodes;
    let requirement_name = '';
    let courses_node = null;
    for (const node of requirement_content) {
      if (node.nodeName == 'requirement_name') { requirement_name = node.textContent;}
      if (node.nodeName == 'courses' && node.hasChildNodes()) { courses_node = node;}
    }
    let data = {'requirement_name':requirement_name, 'courses':courses_node};
    requirement_data.push(data);
  }
  return requirement_data;
}
function readCourses(courses:NodeList) {
  let course_data = [];
  for (const course of  courses) {
    let course_content = course.childNodes;
    let course_name = '';
    let prereqs_node = null;
    let ap_node = null;
    for (const node of course_content) {
      if (node.nodeName == 'course_name') { course_name = node.textContent;}
      if (node.nodeName == 'prereqs' && node.hasChildNodes()) { prereqs_node = node;}
      if (node.nodeName == 'ap' && node.hasChildNodes()) { ap_node = node;}
    }
    let data = {'course_name':course_name, 'prereqs':prereqs_node, 'ap':ap_node};
    course_data.push(data);
  }
  return course_data;
}
function readPrereqs(prereqs:NodeList) {
  let prereq_data = [];
  for (const prereq of prereqs) {
    let prereq_content = prereq.childNodes;
    let prereq_name = '';
    for (const node of prereq_content) {
      if (node.nodeName == 'prereq_name') { prereq_name = node.textContent;}
    }
    prereq_data.push(prereq_name);
  }
  return prereq_data;
}
function readAp(ap:NodeList) {
  let ap_data = [];
  for (const ap_test of ap) {
    let test_content = ap_test.childNodes;
    let test_name = '';
    for (const node of test_content) {
      if (node.nodeName == 'test_name') { test_name = node.textContent;}
    }
    ap_data.push(test_name);
  }
  return ap_data;
}
function addCoursesData(workspace_id:string, response:Document){
  // -- data tree --
  // ex major:major_name
  // -- session catalog ---
  let session_majors:string[] = []; //ex  major
  let session_categories:string[] = []; //ex major/category
  let session_subcategories:string[] = []; //ex major/category/subcategory
  let session_requirements:string[] = []; //ex major/category/subcategory/requirement
  let session_courses:string[] = []; //ex major/category/subcategory/requirement/course
  let session_prereqs:string[] = []; //ex  major/category/subcategory/requirement/course/prereq/course
  let session_ap:string[] = []; //ex  major/category/subcategory/requirement/course/test/testname
  // ---
  let majors = response.getElementsByTagName('major');
  let major_data = readMajors(majors);
  for (const major of major_data) {
    // data tree
    addDataList(workspace_id, `Major:${major.major_name}`);
    // session
    session_majors.push(major.major_name)
    if (major.categories != null) {
      let categories = major.categories.childNodes;
      let category_data = readCategories(categories);
      for (const category of category_data) {
        // data tree
        addDataList(`Major:${major.major_name}`, `Category:${category.category_name}`);
        // session
        session_categories.push(`${major.major_name}/${category.category_name}`)
        if (category.subcategories != null) {
          let subcategories = category.subcategories.childNodes;
          let subcategory_data = readSubcategories(subcategories);
          for (const subcategory of subcategory_data) {
            // data tree
            addDataList(`Category:${category.category_name}`, `Subcategory:${subcategory.subcategory_name}`);
            // session
            session_subcategories.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}`)
            if (subcategory.requirements != null) {
              let requirements = subcategory.requirements.childNodes;
              let requirement_data = readRequirements(requirements);
              for (const requirement of requirement_data) {
                // data tree
                addDataList(`Subcategory:${subcategory.subcategory_name}`, `Requirement:${requirement.requirement_name}`);
                // session
                session_requirements.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}`)
                if (requirement.courses != null) {
                  let courses = requirement.courses.childNodes;
                  let course_data = readCourses(courses);
                  for (const course of course_data) {
                    // data tree
                    addDataList(`Requirement:${requirement.requirement_name}`, `Course:${course.course_name}`);
                    // session
                    session_courses.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}`)
                    if (course.prereqs != null) {
                      // data tree
                      addDataList(`Course:${course.course_name}`, `Prereq:${course.course_name}`);
                      let prereqs = course.prereqs.childNodes;
                      let prereq_data = readPrereqs(prereqs);
                      for (const prereq of prereq_data) {
                        addSpecificData(`Prereq:${course.course_name}`, prereq);
                        // session
                        session_prereqs.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/prereq/${prereq}`)
                      }
                    }
                    if (course.ap != null) {
                      // data tree
                      addDataList(`Course:${course.course_name}`, `Ap:${course.course_name}`);
                      let ap = course.ap.childNodes;
                      let ap_data = readAp(ap);
                      for (const ap_test of ap_data) {
                        addSpecificData(`Ap:${course.course_name}`, ap_test);
                        // session
                        session_ap.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/test/${ap_test}`)
                      }
                    }
                  }
                }  
              }
            }
          }
        }
      }
    }
  }
  addSessionCourses(
    session_majors,
    session_categories,
    session_subcategories,
    session_requirements,
    session_courses,
    session_prereqs,
    session_ap
    );
}            
function updateCoursesData(){
  let workspace_id = 'coursesdata';
  clearData(workspace_id);
  let url_source = '/requestcoursesdata';
  requestAJAX(url_source, workspace_id, addCoursesData);
}

