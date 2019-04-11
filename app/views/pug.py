import json
import os
import sys
sys.path.append('../')

from utils.get_extension_characters import get_extension_charaters, get__extension_charaters_all_contents
def create_tag(tag_name, tag_class, tag_id):
    if tag_id == "NULL" and tag_class == "NULL":
        fp.write("    %s\n" %tag_name)
    if tag_id == "NULL" and tag_class != "NULL": 
        fp.write("    %s.%s\n" %(tag_name, tag_class))
    if tag_id != "NULL" and tag_class == "NULL":
        fp.write("    %s#%s\n" %(tag_name, tag_id))
    if tag_id != "NULL" and tag_class != "NULL":
        fp.write("    %s#%s.%s\n" %(tag_name, tag_class, tag_id))

def generate_pugs():
    fp = open("detect.pug", "w")
    fp.write("extends layout\nblock exhead\n    title\nblock content\n    script(src='../javascripts/xh.js')\n")
    get_extension_charaters()
    path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\characters"
    json_files = os.listdir(path)
    t_set = set()
    for json_file in json_files:
        if (os.path.splitext(json_file)[1] == ".json"):
            json_str = open(path + "\\" + json_file).read()
            dict = json.loads(json_str)
            extension_name = dict["exName"]

            tags = dict["tags"]
            for tag in tags:
                tag_name = tag["tagName"]
                tag_class = tag["class"]
                tag_id = tag["id"]
                if tag_name + "^" + tag_id + "^" + tag_class not in t_set:
                    t_set.add(tag_name + "^" + tag_id + "^" + tag_class)
                    create_tag(tag_name, tag_class, tag_id)

if __name__ == '__main__':
#def generate_pugs_all_contents():
    fp = open("detect.pug", "w")
    get__extension_charaters_all_contents()
    fp.write("extends layout\nblock exhead\n    title\nblock content\n    script(src='../javascripts/xh.js')\n")
    json_str = open("..\\data\\characters_all_contents\\characters_all_contents.json").read()
    dict = json.loads(json_str)
    tags = dict["tags"]
    for tag in tags:
        fp.write(tag)
    
