'''
This is designed for the new Azure Marketplace Bing Search API (released Aug 2012)

Inspired by https://github.com/mlagace/Python-SimpleBing and 
http://social.msdn.microsoft.com/Forums/pl-PL/windowsazuretroubleshooting/thread/450293bb-fa86-46ef-be7e-9c18dfb991ad
'''

import requests # Get from https://github.com/kennethreitz/requests
import string, json
from optparse import OptionParser
import os
import sys

class BingSearchAPI():
    bing_api = "https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Composite?"
    
    def __init__(self, key):
        self.key = key

    def replace_symbols(self, request):
        # Custom urlencoder.
        # They specifically want %27 as the quotation which is a single quote '
        # We're going to map both ' and " to %27 to make it more python-esque
        request = string.replace(request, "'", '%27')
        request = string.replace(request, '"', '%27')
        request = string.replace(request, '+', '%2b')
        request = string.replace(request, ' ', '%20')
        request = string.replace(request, ':', '%3a')
        return request
        
    def search(self, sources, query, params, webfile):
        ''' This function expects a dictionary of query parameters and values.
            Sources and Query are mandatory fields. 
            Sources is required to be the first parameter.
            Both Sources and Query requires single quotes surrounding it.
            All parameters are case sensitive. Go figure.

            For the Bing Search API schema, go to http://www.bing.com/developers/
            Click on Bing Search API. Then download the Bing API Schema Guide
            (which is oddly a word document file...pretty lame for a web api doc)
        '''
        request =  'Sources="' + sources    + '"'
        request += '&Query="'  + str(query) + '"'
        request += '&WebFileType="' + str(webfile) + '"'
        for key,value in params.iteritems():
            request += '&' + key + '=' + str(value) 
        request = self.bing_api + self.replace_symbols(request)
        return requests.get(request, auth=(self.key, self.key)).json


if __name__ == "__main__":
    my_key = "<BING-API-ID>"
    bing = BingSearchAPI(my_key)
    usage = "Usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-s", "--search", dest="search", help="keyword to SEARCH")
    parser.add_option("-f", "--file", dest="webfile", help="Filetype to SEARCH")
    parser.add_option("-n", "--number", dest="num", help="Number of results to SEARCH")
    (options, args) = parser.parse_args()
    if len(sys.argv) != 7:
        parser.error("incorrect number of arguments")
    else:
        params = {'ImageFilters':'"Face:Face"',
              '$format': 'json',
              '$top': options.num,
              '$skip': 0}
        jsonitm = bing.search('web',options.search,params,options.webfile)
        for s in jsonitm["d"]["results"]:
            for t in s["Web"]:
                print t["Url"]
                os.system('wget -P ./files/ '+t["Url"])
