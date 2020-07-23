/// <reference path='toggle.ts'/>
/// <reference path="myAP.ts" />

function clearData(ul_id:string){
  let list = document.getElementById(ul_id);
  if (list == null) { return }
  while (list.firstChild) {
    let child:ChildNode|null = list.lastChild;
    if (child != null) {
      list.removeChild((child));
    }
  }
}
function addSpecificData(ul_id:string, info:string){
  let list = document.getElementById(ul_id);
  if (list == null) { return}
  let data = document.createElement('li');
  data.innerHTML = info;
  list.appendChild(data);
}
function addDataList(parent_ul_id:string, name:string, symbol_type:string, toggle_function:Function){
  let parent = document.getElementById(parent_ul_id);
  if (parent == null) { return}
  let toggle = document.createElement('li');
  let symbol = document.createElement('span');
  symbol.innerHTML = name;
  symbol.className = symbol_type;
  symbol.onclick = ()=> {
    toggle_function(symbol);
  }
  let nested = document.createElement('ul');
  nested.className = 'nested';
  nested.id = name;
  toggle.appendChild(symbol);
  toggle.appendChild(nested);
  parent.appendChild(toggle);
}

 

function addCaretList(parent_ul_id:string, name:string, is_special:boolean, special_id:string){
  let toggle_function = function click(symbol:HTMLElement){
    let data: HTMLElement = symbol.parentElement.querySelector(".nested");
    toggleIt(data);
    symbol.classList.toggle("caret-down");
    if (is_special) {
      if (parent_ul_id == `Year:before`){
        showAPTransfer();
      }
      let element:HTMLElement = document.getElementById(special_id)
      toggleIt(element);
    }
  }
  addDataList(parent_ul_id, name, 'caret', toggle_function)
}

function addStatusList(parent_ul_id:string, name:string, status:boolean){
  let mark = 'xmark';
  if (status) { mark ='checkmark' }
  let toggle_function = function click(symbol:HTMLElement){
    let data: HTMLElement = symbol.parentElement.querySelector(".nested");
    toggleIt(data);
    if (status) {
      symbol.classList.toggle("checkmark_down")
    } else {
      symbol.classList.toggle("xmark-down");
    }
  } 
  addDataList(parent_ul_id, name, mark, toggle_function);
}

