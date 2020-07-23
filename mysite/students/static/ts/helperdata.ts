///<reference path='ajax.ts'/>
///<reference path='dataTree.ts'/>
/// <reference path='sessionData.ts' />
/// <reference path='readXML.ts' />
//helperdata

// my majors
// --- major helper functions ---
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
// ---
// resulting ajax function
function updateMajorData(){
  let workspace_id = 'majorstracked';
  clearData(workspace_id);
  let url_source = '/requestmymajors';
  requestAJAX(url_source, workspace_id, addListedMajors);
}
// my ap
// --- ap helper functions ---
function readMyAP(tests:HTMLCollection) {
  return readMainTags(
    tests,
    ["test_name", "test_score"],
    null
  );
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
// ---
// resulting ajax function
function updateAPData(){
  let workspace_id = '';
  clearData(workspace_id);
  let url_source = '/requestmytransfercredit';
  requestAJAX(url_source, workspace_id, addListedAp);
}
// my planner
// --- planner helper functions ---
function readMyYears(years:HTMLCollection) {
  return readMainTags(
    years,
    ["year_name",],
    ["semesters",],
  );
}
function readMySemesters(semesters:NodeList) {
  return readSubNodeList(
    semesters,
    ["semester_name",],
    null
  );
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
    if (year.year_name == "before") {
      addCaretList(workspace_id, `Year:${year.year_name}`, true, "myapactions");
    } else {
      addCaretList(workspace_id, `Year:${year.year_name}`, false, null);
    }
    // session
    session_years.push(year.year_name)
    if (year.semesters != null) {
      let semesters = year.semesters.childNodes;
      let semester_data = readMySemesters(semesters)
      for (const semester of semester_data) {
        // data tree
        addCaretList(`Year:${year.year_name}`,semester.semester_name, true, "mytermactions");
        // session
        session_semesters.push(`${year.year_name}/${semester.semester_name}`)
      }
    }
  }
  addSessionPlanner(
    session_years,
    session_semesters
  );
}
// resulting ajax function
function updatePlannerData(){
  let workspace_id = 'plannerdata';
  clearData(workspace_id);
  let url_source = '/requestmyplanner';
  requestAJAX(url_source, workspace_id, addPlannerData);
}
// my schedule
// --- schedule helper functions ---
function readMySchedules(schedules:HTMLCollection) {
  return readMainTags(
    schedules,
    ["schedule_name",],
    ["courses",]
  );
}
function readMyCourses(courses:NodeList) {
  return readSubNodeList(
    courses,
    ["course_name",],
    null
  );
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
      session_courses.push(`${schedule.schedule_name}/${course.course_name}`)
    }
  }
  addSessionSchedule(
    session_schedules,
    session_courses,
  );
}
// resulting ajax function
function updateScheduleData(){
  let workspace_id = '';
  clearData(workspace_id);
  let url_source = '/requestmyschedule';
  requestAJAX(url_source, workspace_id, addScheduleData);
}

