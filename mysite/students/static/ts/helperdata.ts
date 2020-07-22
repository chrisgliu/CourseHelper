///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
/// <reference path="sessiondata.ts" />

//helperdata

function addListedMajors(workspace_id:string, response:Document) {
  let session_mymajors:string[] = []
  let majors = response.getElementsByTagName('major') 
  for (const major of majors) {
    session_mymajors.push(major.innerHTML)
  }
  //display majors in tracker
  //add session data
  addSessionMajors(
    session_mymajors
  );
}

// result:
function updateMajorData(){
  let workspace_id = 'majorstracked';
  clearData(workspace_id);
  let url_source = '/requestmymajors';
  requestAJAX(url_source, workspace_id, addListedMajors);
}

function readMyAP(tests:HTMLCollection) {
  let test_data = [];
  for (const test of tests) {
    let test_content = test.childNodes;
    let test_name = '';
    let test_score = null;
    for (const node of test_content) {
      if (node.nodeName == 'test_name'){ test_name = node.textContent; }
      if (node.nodeName == 'test_score'){ test_score = node.textContent;}
    }
    let data = {'test_name':test_name, 'test_score':test_score};
    test_data.push(data);
  }
  return test_data;
}

function addListedAp(workspace_id:string, response:Document) {
  let session_myap:string[] = []
  let tests = response.getElementsByTagName('test') 
  let test_data = readMyAP(tests)
  for (const test of test_data) {
    let info = `${test.test_name}/${test.test_score}`
    session_myap.push(info)
  }
  //display majors in tracker
  //add session data
  addSessionAP(
    session_myap
  );
}

// result:
function updateAPData(){
  let workspace_id = '';
  clearData(workspace_id);
  let url_source = '/requestmytransfercredit';
  requestAJAX(url_source, workspace_id, addListedAp);
}

// --- planner helper functions ---
function readMyYears(years:HTMLCollection) {
  let year_data = [];
  for (const year of years) {
    let year_content = year.childNodes;
    let year_name = '';
    let semesters_node = null;
    for (const node of year_content) {
      if (node.nodeName == 'year_name'){ year_name = node.textContent; }
      if (node.nodeName == 'semesters' && node.hasChildNodes()){ semesters_node = node;}
    }
    let data = {'year_name':year_name, 'semesters':semesters_node};
    year_data.push(data);
  }
  return year_data;
}

function readMySemesters(semesters:NodeList) {
  let semester_data = [];
  for (const semester of semesters) {
    let semester_content = semester.childNodes;
    let semester_name = '';
    for (const node of semester_content) {
      if (node.nodeName == 'semester_name'){ semester_name = node.textContent; }
    }
    semester_data.push(semester_name);
  }
  return semester_data;
}
function addPlannerData(workspace_id:string, response:Document) {
  // --- session catalog ---
  let session_years:string[] = [] // ex year
  let session_semesters:string[] = [] // ex year/semester
  // ---
  let years = response.getElementsByTagName('year');
  let year_data = readMyYears(years);
  for (const year of year_data) {
    // data tree
    addDataList(workspace_id, `Year:${year.year_name}`);
    // session
    session_years.push(year.year_name)
    if (year.semesters != null) {
      let semesters = year.semesters.childNodes;
      let semester_data = readMySemesters(semesters)
      for (const semester of semester_data) {
        // data tree
        addSpecificData(`Year:${year.year_name}`,semester);
        // session
        session_semesters.push(`${year.year_name}/${semester}`)
      }
    }
  }
  addSessionPlanner(
    session_years,
    session_semesters
  );
}

// result:
function updatePlannerData(){
  let workspace_id = 'plannerdata';
  clearData(workspace_id);
  let url_source = '/requestmyplanner';
  requestAJAX(url_source, workspace_id, addPlannerData);
}

// --- schedule helper functions ---
function readMySchedules(schedules:HTMLCollection) {
  let schedule_data = [];
  for (const scedule of schedules) {
    let schedule_content = scedule.childNodes;
    let schedule_name = '';
    let courses_node = null;
    for (const node of schedule_content) {
      if (node.nodeName == 'schedule_name'){ schedule_name = node.textContent; }
      if (node.nodeName == 'courses' && node.hasChildNodes()){ courses_node = node;}
    }
    let data = {'schedule_name':schedule_name, 'courses':courses_node};
    schedule_data.push(data);
  }
  return schedule_data;
}

function readMyCourses(courses:NodeList) {
  let course_data = [];
  for (const course of courses) {
    let course_content = course.childNodes;
    let course_name = '';
    for (const node of course_content) {
      if (node.nodeName == 'course_name'){ course_name = node.textContent; }
    }
    course_data.push(course_name);
  }
  return course_data;
}

function addScheduleData(workspace_id:string, response:Document) {
  // --- session catalog ---
  let session_schedules:string[] = [] // ex sched (semester)
  let session_courses:string[] = [] // ex sched/course
  // ---
  let schedules = response.getElementsByTagName('schedule')
  let schedule_data = readMySchedules(schedules);
  for (const schedule of schedule_data) {
    // session
    session_schedules.push(schedule.schedule_name)
    let courses = schedule.courses.childNodes;
    let course_data = readMyCourses(courses)
    for (const course of course_data) {
      // session
      session_courses.push(course)
    }
  }
  addSessionSchedule(
    session_schedules,
    session_courses,
  );
}

// result:
function updateScheduleData(){
  let workspace_id = '';
  clearData(workspace_id);
  let url_source = '/requestmyschedule';
  requestAJAX(url_source, workspace_id, addScheduleData);
}

