
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
        darkit(thingy);
      } else {
        undarkit(thingy);
      }
    }
  }
  
  function darkmode(){
    toggledark("body");
    toggledark("div");
    toggledark("input");
    toggledark("select");
    toggledark("label");
    toggledark("button");
    toggledark("form");
    toggledark("section");
    toggledark("ul");
    toggledark("li");
  }