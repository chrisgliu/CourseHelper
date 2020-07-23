/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />
/// <reference path="helperButtons.ts" />


function createMajorTracker(workspace_id:string, major_name:string){
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) { return} 
    let tracker = document.createElement("div");
    tracker.className = "hstack tracker";
    let name = document.createElement("label");
    name.innerHTML = major_name;
    let progress = document.createElement("button");
    progress.onclick = ()=> {
        for (const item of actions) { dontShowIt(item);}
        showIt('status');
    }
    progress.className = "bigfield progresscontainer";
    let background = document.createElement("div");
    background.className = "progress";
    let bar = document.createElement("div");
    bar.className = "bar";
    bar.id = `${major_name}-bar`;
    bar.innerHTML = "progress"
    background.appendChild(bar);
    progress.appendChild(background);
    tracker.appendChild(name);
    tracker.appendChild(progress);
    workspace.appendChild(tracker);
}
function showTrackedMajors(){
    clearData("majorstracked");
    let majors = getSessionDataList("mymajor");
    for (const major of majors) {
        createMajorTracker("majorstracked", major);
    }
}
