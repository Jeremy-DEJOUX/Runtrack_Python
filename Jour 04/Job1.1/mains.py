from xml.dom.minidom import parse
import re

file = parse('Jour 04/Job1.1/domains.xml')

column = file.getElementsByTagName("column")

for i in range(len(column)):
    txt = column[i].firstChild.data
    domains = re.findall(".com$|.net$|.fr$|.org$" , txt)
    if domains:
        print(txt)