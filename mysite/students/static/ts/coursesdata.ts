///<reference path='ajax.ts'/>
///<reference path='treedata.ts'/>
// courses tree data
class content {
  key_a:string; key_b:string; key_c:string;
  value_a:any; value_b:any; value_c:any;
  constructor(tag_a:string, tag_b:string, tag_c:string) {
    this.key_a = tag_a; this.key_b = tag_b; this.key_c = tag_c;
    this.value_a = this.value_b = this.value_c = null;
  }
  set assignValA(value:any) { this.value_a = value;}
  set assignValB(value:any) { this.value_b = value;}
  set assignValC(value:any) { this.value_c = value;}
  valueOf(key:string){
    if (key==this.key_a) { return this.value_a; }
    if (key==this.key_b) { return this.value_b; }
    if (key==this.key_c) { return this.value_c; }
  }
}
function readNodeContent(node_content:NodeList, tag_a:string, tag_b:string, tag_c:string){
  let output:content = new content(tag_a, tag_b, tag_c);
  for (const node of node_content) {
    if (node.nodeType == 1) {
      if (node.nodeName == tag_a) { output.assignValA = node; }
      if (node.nodeName == tag_b) { output.assignValB = node; }
      if (node.nodeName == tag_c) { output.assignValC = node; }
    }
  }
  return output;
}
//Major:test
function addCoursesData(workspace_id:string, response:Document){
  let majors = response.getElementsByTagName('major');
  for (const major of majors) {
    let major_content:content = readNodeContent(major.childNodes, 'major_name', 'categories', null);
    let major_name = major_content.valueOf('major_name').nodeValue;
    addDataList(workspace_id, `Major:${major_name}`);
    let categories_node = major_content.valueOf('categories');
    let categories = categories_node.childNodes;
    for (const category of categories) {
      let category_content:content = readNodeContent(category.childNodes, 'category_name', 'subcategories', null);
      let category_name = category_content.valueOf('category_name').nodeValue;
      addDataList(`Major:${major_name}`, `Category:${category_name}`);
      let subcategories_node = category_content.valueOf('subcategories');
      let subcategories = subcategories_node.childNodes;
      for (const subcategory of subcategories) {
        let subcategory_content:content = readNodeContent(subcategory.childNodes, 'subcategory_name', 'requirements', null);
        let subcategory_name = subcategory_content.valueOf('subcategory_name').nodeValue;
        addDataList(`Subcategory:${subcategory_name}`, `Category:${category_name}`)
        let requirements_node = subcategory_content.valueOf('requirements');
        let requirements = requirements_node.childNodes;
        for (const requirement of requirements) {
          let requirement_content:content = readNodeContent(requirement.childNodes, 'requirement_name', 'courses', null);
          let requirement_name = requirement_content.valueOf('requirement_name').nodeValue;
          addDataList(`Subcategory:${subcategory_name}`, `Requirement:${requirement_name}`);
          let courses_node = requirement_content.valueOf('courses');
          let courses = courses_node.childNodes;
          for (const course of  courses) {
            let course_content:content = readNodeContent(course.childNodes, 'course_name', 'prereqs', 'ap');
            let course_name = course_content.valueOf('course_name').nodeValue;
            addDataList(`Requirement:${requirement_name}`, `Course:${course_name}`);
            let prereqs_node = course_content.valueOf('prereqs');
            let prereqs = prereqs_node.childNodes;
            addDataList(`Course:${course_name}`, `Prereq:${course_name}`);
            for (const prereq of prereqs) {
              let prereq_content:content = readNodeContent(prereq.childNodes, 'prereq_name', null, null);
              let prereq_name = prereq_content.valueOf('prereq_name').nodeValue;
              addSpecificData(`Prereq:${course_name}`, prereq_name);
            }
            let ap_node = course_content.valueOf('ap');
            let ap = ap_node.childNodes;
            addDataList(`Course:${course_name}`, `Ap:${course_name}`);
            for (const test of ap) {
              let test_content:content = readNodeContent(test.childNodes, 'test_name', null, null);
              let test_name = test_content.valueOf('test_name').nodeValue;
              addSpecificData(`Ap:${course_name}`, test_name);
            }
          }
        }
      }    
    }
  }
}
function updateCoursesData(){
  let workspace_id = 'coursesdata';
  clearData(workspace_id);
  let url_source = '/requestcoursesdata';
  requestAJAX(url_source, workspace_id, addCoursesData);
}





















