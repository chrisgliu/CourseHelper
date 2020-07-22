
function readXMLNodes(tags:any, subdatatags:string[], subparenttags:string[]){
    let tag_data = [];
    for (const tag of tags) {
        let tag_content = tag.childNodes;
        let subtag_data: { [id: string] : any; } = {};
        for (const node  of tag_content) {
            for (const subtag of subdatatags) {
                if (node.nodeName == subtag) {
                    subtag_data[subtag] = node.textContent;
                }
            }
            if (subparenttags != null) {
                for (const subtag of subparenttags) {
                    if (node.nodeName == subtag) {
                        subtag_data[subtag] = node;
                    }
                }
            }            
        }
        tag_data.push(subtag_data);
    }
    return tag_data;
}

function readMainTags(tags:HTMLCollection, subdatatags:string[], subparenttags:string[]) {
    return readXMLNodes(tags, subdatatags, subparenttags);
}

function readSubNodeList(list:NodeList, subdatatags:string[], subparenttags:string[]) {
    return readXMLNodes(list, subdatatags, subparenttags);
}