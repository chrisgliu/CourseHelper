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

def getXMLComplex(data_set, data_model, **kwargs):
    root = etree.Element(data_set)
    sub_one_ref = kwargs.get('one_ref', None)
    sub_one = kwargs.get('one_data', None)
    sub_two_ref = kwargs.get('two_ref', None)
    sub_two = kwargs.get('two_data', None)
    sub_three_ref = kwargs.get('three_ref', None)
    sub_three = kwargs.get('three_data', None) 
    model = etree.Element(data_model)
    if(sub_one_ref is not None and sub_one is not None):
        subdata_one = etree.Element(sub_one_ref)
        subdata_one.text = sub_one
        model.append(subdata_one)
    if(sub_two_ref is not None and sub_two is not None):
        subdata_two = etree.Element(sub_two_ref)
        subdata_two.text = sub_two
        model.append(subdata_two)
    if(sub_three_ref is not None and sub_three is not None):
        subdata_three = etree.Element(sub_three_ref)
        subdata_three.text = sub_three
        model.append(subdata_three)
    root.append(model)
    the_xml_string = etree.tostring(root, xml_declaration=True)
    return the_xml_string 


        


