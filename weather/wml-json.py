import sys, json, os
import xml.etree.ElementTree as ET

def searchChild(root_node, json_tree):
    for child in root_node:
        json_tree[child.tag] = child.attrib
        if len(child) > 0:
            searchChild(child, json_tree[child.tag]) # recursion
        elif len(child.attrib)== 0:
            json_tree[child.tag] = child.text

################### Main Process ######################### 

if __name__ == "__main__":
    
    if len(sys.argv) == 2:


        if os.path.exists(sys.argv[1]) and sys.argv[1].split('.')[1].lower() == 'xml' : # this file is exist and type xml

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
                    json.dump(jsonDict, file, indent=3)
                    print(f'{fileName}-{i}.json was created!')

            else:
                # there are no fileName.json
                with open(f'{fileName}.json', 'w') as file:
                    json.dump(jsonDict, file, indent=3)
                    print(f'{fileName}.json was created!')   

        else: # this file name isn't exist
            print('File Error :: There is no file in current dirrectory or type is wrong!')
    else:
        print('Argument Error :: Please try $python {fileName.xml}')