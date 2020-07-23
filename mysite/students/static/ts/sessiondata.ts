// adding session data
// --- helper 
function addSessionDataList(data:string[], data_name:string) {
    window.sessionStorage.setItem(data_name, JSON.stringify(data));
}
// ---
function addSessionCourses(
    majors:string[],
    categories:string[],
    subcategories:any[],
    requirements:any[],
    courses:any[],
    prereqs:string[],
    ap:string[]
    ) {
    addSessionDataList(majors, "major");
    addSessionDataList(categories, "category");
    addSessionDataList(subcategories, "subcategory");
    addSessionDataList(requirements, "requirement");
    addSessionDataList(courses, "course");
    addSessionDataList(prereqs, "prereq");
    addSessionDataList(ap, "test");
}
function addSessionMajors(majors:string[]){
    addSessionDataList(majors, "mymajor");
}
function addSessionAP(ap:string[]){
    addSessionDataList(ap, "myap");
}
function addSessionPlanner(
    years:string[],
    semesters:string[]
    ){
    addSessionDataList(years, "myyear");
    addSessionDataList(semesters, "mysemester");
}
function addSessionSchedule(
    schedules:string[],
    courses:string[]
    ){
    addSessionDataList(schedules, "myschedule");
    addSessionDataList(courses, "mycourse");
}
// interacting with session data
function clearSession(){
    window.sessionStorage.clear();
}
function removeSessionData(data_id:string) {
    window.sessionStorage.removeItem(data_id);
}
function getSessionData(data_id:string) {
    let data = window.sessionStorage.getItem(data_id);
    return JSON.parse(data);
}
