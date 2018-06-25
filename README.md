# Data-Wrangling-Project

#Using the mapparser.py here are the different types of tags and their counts:
'osm': 1, 
'note': 1
'meta': 1
'bounds': 1
'node': 1190824
'tag': 709053
'way': 175548
'nd': 1427622
'relation': 987
'member': 31249

#Using the provided tags.py the osm file was checked for problem characters and lower case issue:
'lower': 389904
'lower_colon': 309486
'problemchars': 0
'other': 9663

#Using the provided audit.py several street names were updated from abbreviations to full names.  I added N, S, E, W, Circle, and Highway to the mapping list which updated quite a few more street names.  One could further clean the data by finding addresses that ended with a suite number, and creating a more extensive list 
