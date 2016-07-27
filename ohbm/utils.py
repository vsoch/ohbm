
'''
utils: part of the nidm-api
general functions for the api

'''

from pokemon.skills import get_ascii
import __init__
import xmltodict
import requests
import stat
import json
import os
import re


def get_url(url):
    '''get_url returns a result from a url using requests module
    :param url: the url to retrieve
    '''
    response = requests.get(url)
    if response.status_code == 200:
        result = xmltodict.parse(response.text)
        if "rst" in result:
            result = result['rst']
        if "err" in result:
            message = "%s (%s)" %(result['err']['@msg'],result['err']['@code'])
            get_ascii(name="psyduck",message=message)
        return result


def get_installdir():
    '''get_installdir
       returns installation directory of nidm-api
    '''
    return os.path.dirname(os.path.abspath(__init__.__file__))


def ordered_to_dict(ordered_dict):
    '''ordered_to_dict converts an input ordered dict into a standard dict
    :param ordered_dict: the ordered dict
    '''
    return json.loads(json.dumps(ordered_dict))


def parse_item(result,item):
    '''parse_item is a general function for looking one level
    into a result dictionary, for example returning result['event']
    if it exists, where 'event' is the item. For function calls with
    two levels (['events']['event'] see parse_items.
    :param item: the name of the item (eg, event,exhibitor)
    '''
    if item in result:
        print("Found %s!" %(item))
        result = result[item]
    else:
        print("No %s found." %(item))
    return ordered_to_dict(result)


def parse_items(result,item):
    '''parse_items is a general function for looking TWO levels
    into a result dictionary, for example returning result['events']['event']
    if it exists, where 'event' is the item. For function calls with
    one levels (['event'] see parse_item.
    :param item: the name of the item (eg, event,exhibitor)
    '''
    items = '%ss' %(item)
    if items in result:
        if item in result[items]:
            result = result[items][item]
            print("Found %s %s!" %(len(result),items))
    else:
        print("No %s found." %(items))
    return ordered_to_dict(result)


def capitalize(word):
    '''capitalize an input word.
    :param word: the string to capitalize
    '''
    return word.upper()
