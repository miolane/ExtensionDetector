import json
import os
import re

def get_tags(elements):
    character_set = set()
    tags = []
    for element in elements:
        tag = re.search('<(.*?)>', element).group(0) # split string by "<>"
        id_list = re.findall(r"id=\"(.+?)\"", tag)
        tag_name_list = re.findall(r"<(.+?)\s", tag)
        class_name_list = re.findall(r"class=\"(.+?)\"", tag)
        id = id_list[0] if id_list else "NULL"
        tag_name = tag_name_list[0] if tag_name_list else "NULL"
        class_name = class_name_list[0] if class_name_list else "NULL"

        tag_dict = {}
        tag_dict["tagName"] = tag_name
        tag_dict["class"] = class_name
        tag_dict["id"] = id

        if (tag_name + "^" + id + "^" + class_name not in character_set):
            character_set.add(tag_name + "^" + id + "^" + class_name)
            tags.append(tag_dict)
    return tags



def get_extension_charaters():
    path = "..\\data\\characters\\"
    json_str = open("..\\DOM_changes.json", 'rb').read()
    extensions = json.loads(json_str)
    for (extension_str, urls) in extensions.items():
        extension_name = extension_str.split("/")[-1]
        fp = open(path + extension_name.replace(".crx", ".json"), "w")

        characters = {}
        tags = []
        characters["exName"] = extension_name.split(".")[-2]
        

        adds = []
        modifies = []
        deletes = []
        for (url, ops) in urls.items():
            if ops["add"] != "NULL":
                adds.extend(ops["add"])
            if ops["del"] != "NULL":
                deletes.extend(ops["del"])
            if ops["mod"] != "NULL":
                modifies.extend(ops["mod"])
        tags = get_tags(modifies + deletes)
        characters["tags"] = tags
        fp.write(json.dumps(characters))

def process_blanks(elements):
    element_aligned = []
    for element in elements:
        lines = re.findall('(<.*?>)', element)
        paragraph = ""
        tab = "    "
        for idx, line in enumerate(lines):
            if idx < len(lines)/2:
                line = tab*(idx+1) + line + "\n"
            else:
                line = tab*(len(lines) - idx) + line + "\n"
            paragraph = paragraph + line
        print(paragraph)
        element_aligned.append(paragraph)
    return element_aligned

def get__extension_charaters_all_contents():
    fp = open("..\\data\\characters_all_contents\\characters_all_contents.json", "w")
    json_str = open("..\\DOM_changes.json", 'rb').read()
    extensions = json.loads(json_str)
    characters = {}
    tags = []
    for (extension_str, urls) in extensions.items():
        
        adds = []
        modifies = []
        deletes = []
        for (url, ops) in urls.items():

                adds = adds + ops["add"]
                deletes = deletes + ops["del"]
                modifies = modifies + ops["mod"]
        tags = tags + process_blanks(modifies + deletes)
    characters["tags"] = tags
    fp.write(json.dumps(characters))