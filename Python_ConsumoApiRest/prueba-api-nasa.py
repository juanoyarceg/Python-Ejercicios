import json
import requests
def request(url, api_key):
    querystring = {"sol":"1000","page":"1","api_key":api_key}
    headers = {
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "474bdb77-2e56-4ab4-9264-551e6bc12276,deccf847-020e-401e-88f2-29aa2b8fd946",
        'Host': "api.nasa.gov",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)

data = request("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", "xdgBjiUNKvA2guqECZUAjGmyJJdKb88jpTE8he9p")

def build_web_page(data):
    
    html = "<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n    <ul>\n"
    for photo in data["photos"]:
        html += "        <li>\n            <img src=\"{}\">\n        </li>\n".format(photo["img_src"])
    html += "   </ul>\n</body>\n</html>"
    with open("output.html", "w") as f:
        f.write(html)

build_web_page(data)
