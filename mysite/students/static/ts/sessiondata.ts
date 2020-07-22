function addSessionDataList(data:string[], data_name:string) {
    for (let index = 0; index < data.length; index++) {
        let value = data[index];
        let key = data_name+"-"+index; 
        window.sessionStorage.setItem(key, value)
    }
}

function addSessionCourses(
    majors:string[],
    categories:string[],
    subcategories:string[],
    requirements:string[],
    courses:string[],
    prereqs:string[],
    ap:string[]
    ) {
    addSessionDataList(majors, "major")
    addSessionDataList(categories, "category")
    addSessionDataList(subcategories, "subcategory")
    addSessionDataList(requirements, "requirement")
    addSessionDataList(courses, "course")
    addSessionDataList(prereqs, "prereq")
    addSessionDataList(ap, "test")
}

function clearSession(){
    window.sessionStorage.clear();
}

function removeSessionData(data_id:string) {
    window.sessionStorage.removeItem(data_id)
}
function getSessionData(data_id:string) {
    let data = window.sessionStorage.getItem(data_id)
    return data    
}