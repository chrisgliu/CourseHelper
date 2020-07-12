// --- making a request for data ---
function requestAJAX(url_source:string, data_tag:string, workspace_id:string,
                     add_data_function:(workspace_id:string, info:string)=> void){
  let request:XMLHttpRequest = new XMLHttpRequest();
  request.open('GET', url_source, true);
  request.onload = () => {
    let response:Document | null = request.responseXML;
    if (response != null){
      let data:any = response.getElementsByTagName(data_tag);
      for (let data_instance of data) {
        let info:string = data_instance.innerHTML;
        add_data_function(workspace_id, info)
      }
    }
  }
  request.send();
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
