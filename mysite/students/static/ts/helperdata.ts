///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
//helperdata

function activateHelperButtons() {
    let actions  = ['mymajoractions', 'mytermactions', 'myapactions',
    'tranfercredit', 'status',
    'mycourseoperation'] 
    document.getElementById('mymajorbutton').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('mymajoractions');
    }

    //testing
    document.getElementById('testbuttonterm').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('mytermactions');
    }
    document.getElementById('testbuttonap').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('myapactions');
    }
    document.getElementById('testbuttontranfer').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('tranfercredit');
    }
    document.getElementById('testbuttonstatus').onclick = ()=>{
      for (const item of actions) { dontShowIt(item);}
      showIt('status');
    }
    ///testing
    
    document.getElementById('mycoursesbutton').onclick = ()=>{
      showIt('mycourseoperation');
    }
    document.getElementById('myapbutton').onclick = ()=>{
      showIt('mytestoperation');
    } 
}
 
