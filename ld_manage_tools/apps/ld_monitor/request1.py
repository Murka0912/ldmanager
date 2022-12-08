import requests
from requests.auth import HTTPBasicAuth
import time


def auth(user,password,url):
    basic = HTTPBasicAuth(user,password)
    headers = {
        'accept': 'application/json , text/plain',
        "Authorization": "Basic ZGJvOmRibw==",
    }
    realurl = url+'/api/v1/auth/basic'
    r = requests.get(realurl, headers=headers, auth=basic)
    return r



def request_resp(cook, url, headers):
    realurl = url
    dr = requests.get(realurl,
                     headers=headers, cookies=cook)
    return dr

authurl = 'http://172.29.17.130/landocs.webapi'
url = 'http://dsud-cafk-arh/landocs.webapi.netcore/api/v1/journals/340285/'
listurl = ['http://dsud-cafk-arh/landocs.webapi.netcore/api/v1/me/history',
           'http://dsud-cafk-arh/landocs.webapi.netcore/api/v1/instructions/folder/1999/instructions',
           'http://dsud-cafk-arh/landocs.webapi.netcore/api/v1/deputies',
           'http://dsud-cafk-arh/landocs.webapi.netcore/api/v1/journals/340285'
           ]


a = auth('dba','sql',authurl)
print( a.status_code)