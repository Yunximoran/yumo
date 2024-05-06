import xml.etree.ElementTree as ET

tree = ET.parse("config.xml")


root = tree.getroot()


for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    year = country.find("year").text

    print(rank, name, year)