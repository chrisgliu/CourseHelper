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
function addDataList(parent_ul_id:string, name:string, special:boolean, special_id:string){
  let special_actions = ['mymajoractions', 'mytermactions', 'myapactions',
  'tranfercredit', 'status',
  'mycourseoperation'] 
  
  let parent = document.getElementById(parent_ul_id);
  if (parent == null) { return}
  let toggle = document.createElement('li');
  let symbol = document.createElement('span');
  symbol.innerHTML = name;
  symbol.className = 'caret';
  symbol.onclick = ()=> {
    let data: HTMLElement = symbol.parentElement.querySelector(".nested");
    toggleIt(data);
    if (special) {
      let element:HTMLElement = document.getElementById(special_id)
      for (const item of special_actions) { dontShowIt(item);}
      toggleIt(element);
    }
    symbol.classList.toggle("caret-down");
  }
  let nested = document.createElement('ul');
  nested.className = 'nested';
  nested.id = name;
  toggle.appendChild(symbol);
  toggle.appendChild(nested);
  parent.appendChild(toggle);
}
function addSpecificData(ul_id:string, info:string){
  let list = document.getElementById(ul_id);
  if (list == null) { return}
  let data = document.createElement('li');
  data.innerHTML = info;
  list.appendChild(data);
}
function getSubListNames(parent_ul_id:string){
  let names:string[]= [];
  let parent = document.getElementById(parent_ul_id);
  if (parent == null) { return}
  let data = parent.children;
  for (let index = 0; index < data.length; index++) {
    let listitem = data[index];
    let name = listitem.getElementsByTagName('span')[0].innerHTML;
    names.push(name);
  }
  return names;
}
