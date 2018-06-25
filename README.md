# Data-Wrangling-Project

# Tags and Counts
Using the mapparser.py here are the different types of tags and their counts:
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

# Tag Issues
Using the provided tags.py the osm file was checked for problem characters and lower case issue:
'lower': 389904
'lower_colon': 309486
'problemchars': 0
'other': 9663

# Cleaning the Street Names
Using the provided audit.py several street names were updated from abbreviations to full names.  I added N, S, E, W, Circle, and Highway to the mapping list which updated quite a few more street names.  One could further clean the data by finding addresses that ended with a suite number, county roads and highways that ended with a number, fixing more than the last word, and creating a more extensive list of possible street ending names.
Here are a few updated street names:
6th Ave N => 6th Ave North
Larpenteur Ave W => Larpenteur Ave West
Stinson Blvd => Stinson Boulevard
Here are a few that didn't get updated:
East River Rd/Pkwy => East River Rd/Pkwy
Hopkins Crossroad => Hopkins Crossroad
CR 25 => CR 25

