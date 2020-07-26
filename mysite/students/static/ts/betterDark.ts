/// <reference path="coursesDataTree.ts" />

function darkit(thing:HTMLElement) {
    thing.style.background = "black";
    thing.style.color = "white";
    thing.style.borderColor = "white";
}
function undarkit(thing:HTMLElement) {
    thing.style.background = "transparent";
    thing.style.color = "black";
    thing.style.borderColor = "black";
}

function toggledark(tag:string) {
    let things = document.getElementsByTagName(tag);
    for (let thing of things) {
      let thingy = (<HTMLElement>thing);
      if (thingy.style.background != "black") {
        if (thingy.className != "modal"){
          darkit(thingy);
        }
      } else {
        undarkit(thingy);
      }
    }
  }

  function thisNeedsToBeWhite(thing:HTMLElement){
    if (thing.hasChildNodes){
      for (const child of thing.children) {
        let working_child = (<HTMLElement>child);
        working_child.style.background = "white";
        thisNeedsToBeWhite(working_child);
      }
    }
    else { return;}
  }

  function togglemodal(){
    let things = document.getElementsByClassName("modal")
    let darkmode = document.getElementById("darkmode")
    for (const thing of things) {
      if (darkmode.style.background != "black"){
        let working_thing = (<HTMLElement>thing); 
        thisNeedsToBeWhite(working_thing);
      }
    }
  }
  
  function darkmode(){
    toggledark("body");
    toggledark("input");
    toggledark("select");
    toggledark("label");
    toggledark("button");
    toggledark("section");
    toggledark("ul");
    toggledark("li");
    toggledark("h1");
    toggledark("h2");
    toggledark("span")
    toggledark("b"); 
    toggledark("form");
    toggledark("div")
    togglemodal();
    cleanUpDataTree();  

  }