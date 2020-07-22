///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
//helperdata



function addPlannerData(workspace_id:string, response:Document) {

}
function updatePlannerData(){
  let workspace_id = '';
  clearData(workspace_id);
  let url_source = '/';
  requestAJAX(url_source, workspace_id, addPlannerData);
}




