import os
import json
import re

images_json={}

imgpath = "./images/"

dirs = [d for d in os.listdir(imgpath) if os.path.isdir(os.path.join(imgpath,d))]

for d in dirs:
    
    images_json[d]=[]

    onlyfiles = [f for f in os.listdir(imgpath+d) if os.path.isfile(os.path.join(imgpath+d, f))]
    for f in onlyfiles:
        info = {}
        info["path"] = imgpath+d+"/"+f
        info["filename"] = re.sub("(^[0-9]*|[0-9]*$)","",os.path.splitext(f)[0].replace("LINE_ALBUM","").replace("-","").replace(".","").replace("_","").replace("．",''))
        images_json[d].append(info)


# print(dirs)
# print(onlyfiles)
# print(images_json)
with open("images/img.json","w",encoding="utf-8") as f:
    json.dump(images_json,f)