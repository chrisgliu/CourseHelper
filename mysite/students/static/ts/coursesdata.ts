///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
///<reference path='sessiondata.ts'/>
/// <reference path="readXML.ts" />

// courses tree data

// --- courses data helper functions ---
function readMajors(majors:HTMLCollection) {
  return readMainTags(
    majors,
    ["major_name",],
    ["categories",],
  );
}
function readCategories(categories:NodeList) {
  return readSubNodeList(
    categories,
    ["category_name",],
    ["subcategories",],
  );
}
function readSubcategories(subcategories:NodeList) {
  return readSubNodeList(
    subcategories,
    ["subcategory_name",],
    ["requirements",],
  );
}
function readRequirements(requirements:NodeList) {
  return readSubNodeList(
    requirements,
    ["requirement_name",],
    ["courses",],
  );
}
function readCourses(courses:NodeList) {
  return readSubNodeList(
    courses,
    ["course_name",],
    ["prereqs", "ap"]
  );
}
function readPrereqs(prereqs:NodeList) {
  return readSubNodeList(
    prereqs,
    ["prereq_name",],
    null
  );
}
function readAp(ap:NodeList) {
  return readSubNodeList(
    ap,
    ["test_name",],
    null
  );
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
    addDataList(workspace_id, `Major:${major.major_name}`, false, null);
    // session
    session_majors.push(major.major_name)
    if (major.categories != null) {
      let categories = major.categories.childNodes;
      let category_data = readCategories(categories);
      for (const category of category_data) {
        // data tree
        addDataList(`Major:${major.major_name}`, `Category:${category.category_name}`, false, null);
        // session
        session_categories.push(`${major.major_name}/${category.category_name}`)
        if (category.subcategories != null) {
          let subcategories = category.subcategories.childNodes;
          let subcategory_data = readSubcategories(subcategories);
          for (const subcategory of subcategory_data) {
            // data tree
            addDataList(`Category:${category.category_name}`, `Subcategory:${subcategory.subcategory_name}`, false, null);
            // session
            session_subcategories.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}`)
            if (subcategory.requirements != null) {
              let requirements = subcategory.requirements.childNodes;
              let requirement_data = readRequirements(requirements);
              for (const requirement of requirement_data) {
                // data tree
                addDataList(`Subcategory:${subcategory.subcategory_name}`, `Requirement:${requirement.requirement_name}`, false, null);
                // session
                session_requirements.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}`)
                if (requirement.courses != null) {
                  let courses = requirement.courses.childNodes;
                  let course_data = readCourses(courses);
                  for (const course of course_data) {
                    // data tree
                    addDataList(`Requirement:${requirement.requirement_name}`, `Course:${course.course_name}`, false, null);
                    // session
                    session_courses.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}`)
                    if (course.prereqs != null) {
                      // data tree
                      addDataList(`Course:${course.course_name}`, `Prereq:${course.course_name}`, false, null);
                      let prereqs = course.prereqs.childNodes;
                      let prereq_data = readPrereqs(prereqs);
                      for (const prereq of prereq_data) {
                        addSpecificData(`Prereq:${course.course_name}`, prereq.prereq_name);
                        // session
                        session_prereqs.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/prereq/${prereq.prereq_name}`)
                      }
                    }
                    if (course.ap != null) {
                      // data tree
                      addDataList(`Course:${course.course_name}`, `Ap:${course.course_name}`, false, null);
                      let ap = course.ap.childNodes;
                      let ap_data = readAp(ap);
                      for (const ap_test of ap_data) {
                        addSpecificData(`Ap:${course.course_name}`, ap_test.test_name);
                        // session
                        session_ap.push(`${major.major_name}/${category.category_name}/${subcategory.subcategory_name}/${requirement.requirement_name}/${course.course_name}/test/${ap_test.test_name}`)
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
// resulting ajax function
function updateCoursesData(){
  let workspace_id = 'coursesdata';
  clearData(workspace_id);
  let url_source = '/requestcoursesdata';
  requestAJAX(url_source, workspace_id, addCoursesData);
}

