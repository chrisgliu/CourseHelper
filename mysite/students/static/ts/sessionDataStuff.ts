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
    addSessionDataList(ap, "ap");
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
function addAPTranferSessionData(courses:string[], ap_test:string){
    addSessionDataList(courses, `mycourseap-${ap_test}`)
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
function readMySessionString(data_string:string) {
    let data_content = data_string;
    let output:string[] = [];
    while (data_content.indexOf("/") != -1) {
        let data = data_content.substring(0, data_content.indexOf("/")); 
        output.push(data);
        data_content = data_content.substring(data_content.indexOf("/")+1);
    }
    output.push(data_content); 
    return output;
}

function getSubSessionData(data_id:string){
   let data = getSessionData(data_id);
   let subdata:string[] = [];
   for (const info of data) { subdata.push(info[0]); }
   return subdata;
}
