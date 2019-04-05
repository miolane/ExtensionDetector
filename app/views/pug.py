import json
import os
def create_tag(f, tag_name, tag_class, tag_id):
    if tag_id == "NULL":
        fp.write("    %s.%s\n" %(tag_name, tag_class))
    else:
        fp.write("    %s#%s.%s\n" %(tag_name, tag_class, tag_id))

if __name__ == '__main__':
    fp = open("detect.pug", "w")
    fp.write("extends layout\nblock exhead\n    title\nblock content\n    script(src='../javascripts/xh.js')\n")
    path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\detect"
    json_files = os.listdir(path)
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
                create_tag(fp, tag_name, tag_class, tag_id)
    