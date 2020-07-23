/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />
/// <reference path="helperButtons.ts" />
/// <reference path="myYears.ts" />



function createAPTracker(workspace_id:string, test_name:string, score:string){
    let workspace = document.getElementById(workspace_id);
    if (workspace == null) { return} 
    let ap = document.createElement("div");
    ap.className = "hstack";
    let test = document.createElement("label");
    test.innerHTML = test_name;
    let credit = document.createElement("button");
    credit.innerHTML = score;
    credit.onclick = ()=> {
        toggleShow('tranfercredit');
        showTranferCourses(test_name);
    }
    ap.appendChild(test);
    ap.appendChild(credit);
    workspace.appendChild(ap);
}
function showAPTransfer(){
    clearData("myaptests");
    let ap_data = getSessionData("myap");
    if (ap_data == null) { return}
    for (const test of ap_data) {
        if (test != null) {
            let test_content = readMySessionString(test);
            let test_name = test_content[0];
            let score = test_content[1];
            createAPTracker("myaptests", test_name, score);
        } 
    }
}
