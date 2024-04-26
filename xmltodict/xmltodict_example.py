# import xml.etree.ElementTree as ET
# from lxml import etree as ET
import xmltodict
from rich import print
# Get XML Data
stream = open('sample.xml', 'r')

# Parse data into ElementTree object
xml = ET.parse(stream)

# Get the 'root' element object
root = xml.getroot()

# Iterate through all child elements
for i in root:
    print(ET.tostring(i))
    print()

    print(i.get('id'))




# name = input('input your name: ')

# if name == 'nick':
#     print(1, name)
# elif name =='nick':
#     print(name)
# else:
#     print('no name found')