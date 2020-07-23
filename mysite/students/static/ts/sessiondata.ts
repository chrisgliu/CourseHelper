// adding session data
// --- helper 
function addSessionDataList(data:string[], data_name:string) {
    for (let index = 0; index < data.length; index++) {
        let value = data[index];
        let key = data_name+"-"+index; 
        window.sessionStorage.setItem(key, value)
    }
}
// ---
function addSessionCourses(
    majors:string[],
    categories:string[],
    subcategories:string[],
    requirements:string[],
    courses:string[],
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
    return data;
}
function readSessionDataList(data_name:string, del:boolean){
    let values:string[] = [];
    let index = 0;
    let key = data_name+"-"+index
    let data = getSessionData(key);
    if (del) { removeSessionData(key); }
    while (data != null) {
        values.push(data);
        index += 1;
        key = data_name+"-"+index;
        data = getSessionData(key);
        if (del) { removeSessionData(key); };
    }
    return values;
}
function getSessionDataList(data_name:string){
     return readSessionDataList(data_name, false);
}
function removeSessionDataList(data_name:string){
    return readSessionDataList(data_name, true);
}
