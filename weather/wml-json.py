import sys, json, os
import xml.etree.ElementTree as ET

def searchChild(root_node, json_tree):
    for child in root_node:
        json_tree[child.tag] = child.attrib
        if len(child) > 0:
            searchChild(child, json_tree[child.tag])
        elif len(child.attrib)== 0:
            json_tree[child.tag] = child.text

################### Main Process ######################### 

if __name__ == "__main__":
    
    fileName, fileType = sys.argv[1].split('.')
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    jsonDict = {}


    searchChild(root, jsonDict)

    if os.path.exists(f'{fileName}.json'):
        # there are fileName.json, create new fileName
        i = 1
        while os.path.exists(f'{fileName}-{i}.json'):
            i += 1
        with open(f'{fileName}-{i}.json', 'w') as file:
            json.dump(jsonDict, file, indent=4)
            print(f'{fileName}-{i}.json was created!')

    else:
        # there are no fileName.json
        with open(f'{fileName}.json', 'w') as file:
            json.dump(jsonDict, file, indent=3)
            print(f'{fileName}.json was created!')            