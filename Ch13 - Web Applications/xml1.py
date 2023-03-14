import xml.etree.ElementTree as ET

data = """
<person>
    <name>Danilo</name>
    <phone type="int1"> 
        + 381 69 2409 297
    </phone>
    <email hide="yes"/>
</person>"""

tree = ET.fromstring(data)

print("Name: ", tree.find("name").text)
print("Attr: ", tree.find("email").get("hide"))