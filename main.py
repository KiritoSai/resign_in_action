# -*- coding: utf8 -*-
# python >=3.8

import requests
import json
import sys

if __name__ == "__main__":
    notice = {
        "msg_type": "text",
        "content": {
            "text": "补打卡"
        }
    }
    url = ''.join(sys.argv[1])
    r = requests.post(url,data=json.dumps(notice))
    print(r.text)