/// <reference path='toggle.ts'/>

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

let special_actions = ['mymajoractions', 'mytermactions', 'myapactions',
  'tranfercredit', 'status',
  'mycourseoperation'] 

function addCaretList(parent_ul_id:string, name:string, is_special:boolean, special_id:string){
  let toggle_function = function click(symbol:HTMLElement){
    let data: HTMLElement = symbol.parentElement.querySelector(".nested");
    toggleIt(data);
    symbol.classList.toggle("caret-down");
    if (is_special) {
      let element:HTMLElement = document.getElementById(special_id)
      for (const item of special_actions) { dontShowIt(item);}
      toggleIt(element);
    }
  }
  addDataList(parent_ul_id, name, 'caret', toggle_function)
}

function addStatusList(parent_ul_id:string, name:string, status:string){
  let toggle_function = function click(symbol:HTMLElement){
    let data: HTMLElement = symbol.parentElement.querySelector(".nested");
    toggleIt(data);
  } 
  addDataList(parent_ul_id, name, status, toggle_function);
}

