import requests
import urllib
from CodeTable import settings

'''
    code to compile , run the code
'''

HE_API_COMPILE_URL = 'http://api.hackerearth.com/code/compile/'
HE_AIP_RUN_URL = 'http://api.hackerearth.com/code/run/'

def compile(code,language,inp):
    '''

    :param code:
    :param language:
    :param inp:
    :return:
    '''

    data = {
        'client_secret': settings.HE_CLIENT_SECRET_KEY,
        'async': 0,
        'source': code,
        'lang': language,
        'time_limit': 5,
        'memory_limit': 262144,
    }


    r = requests.post(HE_API_COMPILE_URL,data=data)
    return r.json()


def run(code,language,inp):
    '''

    :param code:
    :param language:
    :param inp:
    :return:
    '''
    data = {
        'client_secret': settings.HE_CLIENT_SECRET_KEY,
        'async': 0,
        'source': code,
        'lang': language,
        'input':inp,
        'time_limit': 5,
        'memory_limit': 262144,
    }
    r = requests.post(HE_AIP_RUN_URL,data=data)
    return r.json()