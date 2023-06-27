import feedparser
import sys
import requests
import json
import os
d = feedparser.parse(str(sys.argv[1]))
data = {}
if os.path.isfile(str(sys.argv[3])) == False:
    data["embeds"] = [
    {
        "footer": {
            "text": d.entries[0].published
        },
        "description" : d.entries[0].description,
        "title" : d.entries[0].title,
        "url" : d.entries[0].link
    }
    ]
    result = requests.post(str(sys.argv[2]), json = data)
    f = open(sys.argv[3],'w')
    f.write(str(d.entries[0].published))
    f.close()
else:
    f = open(sys.argv[3],"r")
    pub = f.read()
    f.close()
    if d.entries[0].published != pub:
        i = 0
        f = open(sys.argv[3],'w')
        f.write(str(d.entries[0].published))
        f.close()
        while d.entries[i].published != pub:
            data = {}
            data["embeds"] = [
            {
                "footer": {
                    "text": d.entries[0].published
                },
                "description" : d.entries[i].description,
                "title" : d.entries[i].title,
                "url" : d.entries[i].link
            }
            ]
            result = requests.post(str(sys.argv[2]), json = data)
            i = i + 1
