list_name = ['string,', 'another_string', 'and_etc']
unwanted_element = ','
element_to_replace = ''  # nothing if we want to remove
list_name = [elem.replace(unwanted_element, element_to_replace) for elem in list_name]
print(list_name)