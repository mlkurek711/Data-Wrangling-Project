import xml.etree.cElementTree as ET
from collections import defaultdict
import re
#import pprint

OSMFILE = "C:/Users/Misty/Documents/Udacity/Data_Wrangling_Project/MPLS.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

#list of expected how street names will end
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Circle", "North", "South", "East", "West", "Northeast",
            "Northwest", "Southeast", "Southwest", "Highway"]

#how to fix unexpected street names
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "Rd": "Road",
            "Blvd": "Boulevard",
            "Dr": "Drive",
            "Dr.": "Drive",
            "Ct": "Court",
            "Ct.": "Court",
            "Pl": "Place",
            "Ln": "Lane",
            "Tr": "Trail",
            "Pkwy": "Parkway",
            "N": "North",
            "S": "South",
            "E": "East",
            "W": "West",
            "NE": "Northeast",
            "NW": "Northwest",
            "SE": "Southeast",
            "SW": "Southwet",
            "Hwy": "Hihgway"
            }

#check to see if street names are expected; if not added to list
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

#check if element is street name
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

#check if street name and is not expected
def audit(osmfile):
    osm_file = open(osmfile, "r", encoding="utf8")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return (street_types)

#print street names that don't fit expected names
print(audit(OSMFILE))

#update the street names if they aren't expected
def update_name(name, mapping):
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        if street_type in mapping.keys():
            name = re.sub(street_type, mapping[street_type], name)
    return name

#print updated names
update_street = audit(OSMFILE)
for street_type, ways in update_street.items():
    for name in ways:
        better_name = update_name(name, mapping)
        print(name, "=>", better_name)