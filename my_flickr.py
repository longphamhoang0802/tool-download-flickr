import os
from pathlib import Path
import requests
import json

# import time
# import sys
# from flask import Flask, request, Response

# from flask_cors import CORS

# data = 1 #cookies

url = 'https://api.flickr.com/services/rest'


def filter_image(keyword_search):

    params = {
        "sort": "relevance",
        "parse_tags": 1,
        "content_type": '0,1,2,3',
        "extras": "can_comment,can_print,count_comments,count_faves,description,isfavorite,license,media,needs_interstitial,owner_name,path_alias,realname,rotation,url_sq,url_q,url_t,url_s,url_n,url_w,url_m,url_z,url_c,url_l",
        "per_page": 15,
        "page": 1,
        "lang": "vi-VN",
        "orientation": "landscape,square,panorama",
        "media": "photos",
        "text": keyword_search,
        "safe_search": 3,
        "view_all": 1,
        "viewerNSID": "",
        "method": "flickr.photos.search",
        "csrf": "",
        # self.data["api_key"],  # phải sửa
        "api_key": "5ffe30257118bd128862db7baa81565b",
        "format": "json",
        "hermes": 1,
        "hermesClient": 1,
        # self.data["reqId"],  # phải sửa
        "reqId": "919ce8ef-817c-42f5-9b9f-b9e0d7aed977",
        "nojsoncallback": 1,
        "dimension_search_mode": "min",
        "height": "1024"
    }

    return params


class GetData:

    def get_and_download_image():
        keyword_search = input("nhập text: ")
        req = requests.Session()

        res = req.get(url=url, params=filter_image(keyword_search))
        # print(res)

        response = json.loads(res.content)
        # print(response)

        photos_info = response['photos']
        photos = photos_info['photo']

        for photo in photos:
            id_photo = photo['id']
            url_l_photo = photo['url_l']

            file_name = '{}.jpg'.format(id_photo)
            if os.path.exists(file_name) == False:
                with open(file_name, 'wb') as f:
                    f.write(requests.get(url_l_photo).content)


if __name__ == '__main__':

    GetData.get_and_download_image()
