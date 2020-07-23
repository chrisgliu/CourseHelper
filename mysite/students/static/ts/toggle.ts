// show and don't show operations

function showIt(id: string){
    let element = document.getElementById(id);
    if (element == null){ return}
    element.style.display = 'block'
}
function dontShowIt(id: string){
    let element = document.getElementById(id);
    if (element == null){ return}
    element.style.display = 'none'
}
function toggleIt(element: HTMLElement){
    if (element == null){ return}
    if (element.style.display === 'block'){
        element.style.display = 'none';
    } else {
        element.style.display = 'block';
    }
}
function toggleShow(id: string){
    let element = document.getElementById(id);
    toggleIt(element)
}
