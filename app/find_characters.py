import json
import os
import re

def get_tags(elements):
    character_dict = {}
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

        if (tag_name + "^" + id + "^" + class_name not in character_dict):
            character_dict[tag_name + "^" + id + "^" + class_name] = 1
            tags.append(tag_dict)
    return tags



if __name__ == '__main__':
    path = ".\\characters\\"
    json_str = open("DOM_changes.json", 'rb').read()
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