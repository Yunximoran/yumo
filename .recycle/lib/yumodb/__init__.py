import xml.etree.ElementTree as et

tree = et.parse('../../yumo.xml')

root = tree.getroot()

database = root.find('database')

host = database.find('host').text
redisConfig = database.find("redis")
mysqlConfig = database.find("mysql")



