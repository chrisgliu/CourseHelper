// --- displaying data ---
function clearWorkSpace(workspace_id:string) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null){ return}
    while (workspace.firstChild) {
        let child:ChildNode | null= workspace.lastChild
        if (child != null){
            workspace.removeChild(child);
        }
    }
    let header = document.createElement('th')
    header.innerHTML = workspace_id
    workspace.appendChild(header)
}


function addData(workspace_id:string, info:string) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null){ return}
    let data = document.createElement('td')
    data.innerHTML = info
    workspace.appendChild(data)
}


function readXMLData(workspace_id:string, xml_data:Document, data_tag:string){
    let data: any = xml_data.getElementsByTagName(data_tag);
    for (let data_instance of data) {
        let info = data_instance.innerHTML;
        addData(workspace_id, info);
    }
}

// --- making a request for data ---
function requestAJAX(url_source:string, data_tag:string, work_space_id:string){
    let request:XMLHttpRequest = new XMLHttpRequest();
    request.open('GET', url_source, true);
    request.onload = () => {
        let response:Document | null = request.responseXML;
        if (response != null){
            readXMLData(work_space_id, response, data_tag);
        }
    }
    request.send();
}   


function substituteChar(message:string, spot:number, item:string){
    let before:string = message.substring(0, spot);
    let after:string = message.substring(spot+1);
    let result:string = before + item + after;
    return result
}


function substituteURLSpace(message:string){
    let edited_message: string = message;
    for (let index = 0; index < message.length; index++) {
        let char:string = message.charAt(index);
        if (char == ' '){
            edited_message = substituteChar(edited_message, index, '%20');
        }
    }
    return edited_message;
}

// --- request functions ---
function requestMajors(workspace_id:string){
    requestAJAX('/requestmajors/', 'major', workspace_id);
}


function requestCategories(workspace_id:string, parent_name:string){
    let name:string = substituteURLSpace(parent_name);
    requestAJAX(`/requestcategories/${name}/`, 'category', workspace_id);
}


function requestSubcategories(workspace_id:string, parent_name:string){
    let name:string = substituteURLSpace(parent_name);
    requestAJAX(`/requestsubcategories/${name}/`, 'subcategory', workspace_id); 
}


function requestRequirements(workspace_id:string, parent_name:string){
    let name:string = substituteURLSpace(parent_name);
    requestAJAX(`/requestrequirements/${name}/`, 'requirement', workspace_id); 
}


function requestCourses(workspace_id:string, parent_name:string){
    let name:string = substituteURLSpace(parent_name);
    requestAJAX(`/requestcourses/${name}/`, 'course', workspace_id); 
}


function requestPrereqs(workspace_id:string, parent_name:string){
    let name:string = substituteURLSpace(parent_name);
    requestAJAX(`/requestprereqs/${name}/`, 'prereq', workspace_id); 
}


function requestAP(workspace_id:string, parent_name:string){
    let name:string = substituteURLSpace(parent_name);
    requestAJAX(`/requestap/${name}/`, 'test', workspace_id);
}


