// --- displaying data ---
function clearWorkSpace(workspace_id:string, header_id:string) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null){ return}
    let header = workspace.querySelector(header_id);
    let copy = header.cloneNode(true);
    while (workspace.firstChild) {
        let child:ChildNode | null= workspace.lastChild;
        if (child != null){
            workspace.removeChild(child);
        }
    }
    workspace.appendChild(copy);
}


function addData(workspace_id:string, info:string) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null){ return}
    let data = document.createElement('td');
    data.className = info;
    let button = document.createElement('button')
    let classes:DOMTokenList = button.classList
    classes.add('btn')
    classes.add('btn-submit')
    button.innerHTML = info;
    button.onclick = () => {
        workspace.getElementsByClassName(info)[0].remove()
    }
    data.appendChild(button)
    workspace.appendChild(data);
}

// --- making a request for data ---
function requestAJAX(url_source:string, data_tag:string, workspace_id:string){
    let request:XMLHttpRequest = new XMLHttpRequest();
    request.open('GET', url_source, true);
    request.onload = () => {
        let response:Document | null = request.responseXML;
        if (response != null){
            let data:any = response.getElementsByTagName(data_tag);
            for (let data_instance of data) {
                let info = data_instance.innerHTML;
                addData(workspace_id, info);
            }
        }
    }
    request.send();
    // cant return value in asynchronous request
}   

function substituteChar(message:string, spot:number, item:string){
    let before:string = message.substring(0, spot);
    let after:string = message.substring(spot+1);
    let result:string = before + item + after;
    return result;
}


function checkFoWhitespace(message:string){
    return message.indexOf(' ') !== -1;
}


function substituteURLSpace(message:string){
    let edited_message: string = message;
    if (checkFoWhitespace(message)){
        for (let index = 0; index < message.length; index++) {
            let char:string = message.charAt(index);
            if (char == ' '){
                edited_message = substituteChar(edited_message, index, '%20');
            }
        }
    }
    return edited_message;
}
// retrieving listed data
function retrieveData(workspace_id:string) {
    let workspace = document.getElementById(workspace_id);
    if (workspace == null){ return}
    let info_list = [];
    let data = workspace.children;
    for (let index = 1; index < data.length; index++) {
        const info = data[index].getElementsByTagName('button')[0].innerHTML;
        info_list.push(info);
    }
    return info_list;
}

