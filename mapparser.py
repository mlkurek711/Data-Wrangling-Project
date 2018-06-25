import xml.etree.cElementTree as ET

tags = {}
def count_tags(filename):
        # YOUR CODE HERE
    for event, elem in ET.iterparse(filename, events=('start',)):
        if elem.tag in tags.keys():
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    print(tags)
    #return tags

count_tags("C:/Users/Misty/Documents/Udacity/Data_Wrangling_Project/MPLS.osm")