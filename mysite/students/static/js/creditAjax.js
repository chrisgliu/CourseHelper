
function clearWorkSpace(){
    let workspace = document.getElementById("workspace");
    while (workspace.firstChild) {
        workspace.removeChild(workspace.lastChild);
    }
}
function addData(info){
    let data = document.createElement('li')
    data.className = "courses_data"
    data.innerHTML = info
    document.getElementById("workspace").appendChild(data);
}
function addXMLDataList(xml_data, data_tag){
    clearWorkSpace();
    data = xml_data.getElementsByTagName(data_tag);
    for (let data_instance of data) {
        info = data_instance.innerHTML
        addData(info)
    }
}

function requestAJAX(url_source, data_tag){
    let request = new XMLHttpRequest();
    request.open('GET', url_source, true);
    request.onload = () => {
        let response = request.responseXML;
        addXMLDataList(response, data_tag)
    }
    request.send()
}

function substituteChar(message='', spot=0, item=''){
    let before = message.substring(0, spot);
    let after = message.substring(spot+1);
    let result = before + item + after;
    return result;
}
function addURLspace(message=''){
    let edited_message = message;
    for (let index = 0; index < message.length; index++) {
        let char = message.charAt(index);
        if (char == ' '){
            edited_message = substituteChar(edited_message, index, '%20')
        }
    }
    return edited_message
}
function requestMajors(){
    let test = 'Natural Sciences'
    console.log(addURLspace(test))
    
    requestAJAX('/courses/requestmajors/', 'major')
}
function requestCategories(){
    requestAJAX('/courses/requestcategories/EXAMPLE/', 'category')
}
function requestSubcategories(){
    requestAJAX('/courses/requestsubcategories/GED/', 'subcategory') 
}
function requestRequirements(){
    requestAJAX('/courses/requestrequirements/Natural%20Sciences/', 'requirement') 
}
function requestCourses(){
    requestAJAX('/courses/requestcourses/Lab/', 'course') 
}
function requestPrereqs(){
    requestAJAX('/courses/requestprereqs/Biology%201101/', 'prereq') 
}
function requestAP(){
    requestAJAX('/courses/requestap/Math%201152/', 'test') 
}
