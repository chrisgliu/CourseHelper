/// <reference path="dataTree.ts" />
/// <reference path="sessionData.ts" />
/// <reference path="helperButtons.ts" />


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
    }
    ap.appendChild(test);
    ap.appendChild(credit);
    workspace.appendChild(ap);
}
function showAPTransfer(){
    clearData("myaptests");
    let ap_data = getSessionDataList("myap");
    for (const test of ap_data) {
        let test_name = test.substring(0, test.indexOf("/"));
        let score = test.substring(test.indexOf("/")+1);
        createAPTracker("myaptests", test_name, score);
    }
}
