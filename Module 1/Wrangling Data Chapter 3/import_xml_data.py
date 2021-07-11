import xml.etree.ElementTree as ET

tree = ET.parse('data\data-text.xml')
root = tree.getroot()

data = root.find('Data')

counter = 0
for observation in data:        
    counter += 1
    for child in observation:
        print(child.tag, child.attrib)

print(counter)
    
