#!/usr/bin/env python
import json
import urllib
import pycurl
doc = {
      "description": "the description for this gist",
        "public": 'true',
          "files": {
                "file1.txt": {
                        "content": "String file contents"
                            }
                  }
          }
_doc = urllib.urlencode(doc)
a = pycurl.Curl()
a.setopt(a.URL,'https://api.github.com/gists?access_token=2d4d4fbca12987836ffda997e98338d2fe943d30')
a.setopt(a.POST,1)
a.setopt(a.POSTFIELDS,_doc)
a.perform()
