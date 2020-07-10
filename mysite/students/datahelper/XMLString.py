from lxml import etree

def getXMLString(data_list, data_set, data_model):
    root = etree.Element(data_set)
    length = etree.Element('length')
    length.text = str(len(data_list))
    root.append(length)
    for instance in data_list:
        model = etree.Element(data_model)
        model.text = instance       
        root.append(model)
    the_xml_string = etree.tostring(root, xml_declaration=True)
    return the_xml_string

def getXMLComplex(data_set, data_model, **kwargs)
    root = etree.Element(data_set)
    subdata_one_ref = kwargs.get('one_ref', None)
    subdata_one = kwargs.get('one_data', None)
    subdata_two_ref = kwargs.get('two_ref', None)
    subdata_two = kwargs.get('two_data', None)
    subdata_three_ref = kwargs.get('three_ref', None)
    subdata_three = kwargs.get('three_data', None) 
    model = etree.Element(data_model)
    if(subdata_one_ref is not None and sub_one is not None):
        sub_one = etree.Element(subdata_one_ref)
        sub_one.text = subdata_one
        model.append(sub_one)
    if(subdata_two is not None and sub_two is not None):
        sub_two = etree.Element(subdata_two_ref)
        sub_two.text = subdata_two
        model.append(sub_two)
    if(subdata_three_ref is not None and sub_three is not None):
        sub_three = etree.Element(subdata_three_ref)
        sub_three.text = subdata_three
        model.append(sub_three)
    root.append(model)
    the_xml_string = etree.tostring(root, xml_declaration=True)
    return the_xml_string 


        


