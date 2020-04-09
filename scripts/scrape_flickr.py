import subprocess
import sys

GALLERY_DL_FOLDER = "./gallery-dl/"

# write config file
config = """
{{
    "extractor":
    {{
        "base-directory": "{}",
        "directory": ["output"],
        "postprocessors": null,
        "archive": null,
        "cookies": null,
        "cookies-update": false,
        "proxy": null,
        "skip": true,
        "sleep": 0,

        "flickr":
        {{
            "access-token": null,
            "access-token-secret": null,
            "videos": true,
            "size-max": null
        }}
    }},

    "output":
    {{
        "mode": "auto",
        "progress": true,
        "shorten": true,
        "log": "[{{name}}][{{levelname}}] {{message}}",
        "logfile": null,
        "unsupportedfile": null
    }},

    "netrc": false
}}
""".format(
    GALLERY_DL_FOLDER
)

text_file = open("gallery-dl.conf", "w")
n = text_file.write(config)
text_file.close()

# run gallery-dl to scrape flickr
flickr_groups = [
    "https://www.flickr.com/groups/979936@N25/",
    "https://www.flickr.com/groups/2297498@N20/",
    "https://www.flickr.com/groups/1003995@N21/",
    "https://www.flickr.com/groups/375216@N23/",
]

ct = 0
for url in flickr_groups:
    scrapeCommand = "gallery-dl --range 1-5000 -c gallery-dl.conf {}".format(
        url)
    process = subprocess.Popen(scrapeCommand.split(), stdout=subprocess.PIPE)
    for line in iter(process.stdout.readline, b""):
        sys.stdout.write(line.decode("utf-8"))
        ct += 1
        if ct % 200 == 0:
            print("Downloaded {} images thus far.".format(ct))
    print("{}\n has completed with error code: {}".format(
        scrapeCommand, process.wait()))
