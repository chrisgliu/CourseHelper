// --- making a request for data ---
function requestAJAX(url_source:string, workspace_id:string, 
                     add_data_function:(workspace_id:string, response:Document)=> void){
  let my_request:XMLHttpRequest = new XMLHttpRequest();
  my_request.open('GET', url_source, true);
  my_request.onload = () => {
    if (my_request.status == 200){
      let response:Document | null = my_request.responseXML;
      if (response != null){
        add_data_function(workspace_id, response)
      }
    }
  }
  my_request.send();
  // cant return value in an asynchronous request
}
// --- spaces in url_source ---
function substituteChar(message:string, spot:number, item:string){
  let before:string = message.substring(0, spot)
  let after:string = message.substring(spot+1);
  let result:string = before + item + after;
  return result;
}
function substituteURLSpace(message:string){
  let edited_message:string = message;
  if (message.indexOf(' ')==-1) {
    return message
  }
  for (let index = 0; index < message.length; index++) {
      let char:string = message.charAt(index);
      if (char == ' '){
          edited_message = substituteChar(edited_message, index, '%20');
      }
  }
  return edited_message;
}
