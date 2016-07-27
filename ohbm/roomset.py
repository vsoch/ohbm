'''
roomset: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class Roomset():

    def __init__(self,api=None):
        if api == None:
            print("Please use this module from ohbm.api")
        else:
           self.api = api

    def get_result(self,url,args=None):
        '''get_result takes a url and adds the apiKey for the get_result from utils
        :param url: the url to get the result for
        :param args: a dictionary of {"argumentName":value} to pass to the URL
        '''
        if args != None:
            for arg_name,arg_value in args.iteritems():
                if arg_value != None:
                    url = "%s&%s=%s" %(url,arg_name,arg_value)
        url = "%s&apiKey=%s" %(url,self.api.key)
        return get_url(url)
 

    def getRoomsets(self,postFlag=None):
        '''getRoomSets
        Returns an XML payload containing a full listing of all Room Set data.
        Sample Request URL: http://.../?do=cnt.getservice&service=getRoomSets

        Parameter Options:
        :param postFlag: 0 or 1 (represents true or false).
        '''
        url = "%s/?do=cnt.getservice&service=getRoomSets" %(self.api.base)
        args = {"postFlag":postFlag}
        result = self.get_result(url,args)
        # Note to developer - testing this returned count of 0, if the data structure is equivalent
        # to result['roomSets']['roomSet'] then you can do parse_item(result,'roomSet')
        return ordered_to_dict(result)


    def getRoomset(self,roomSetID):
        '''getRoomSet
        Returns an XML payload containing a full listing of one Room Set. Room Set data consists primarily
        of Room, Location, Room Set Details (supplies), and Vendors. Note: The result set provides urls to the
        figures or documents which are actual files.
        Sample Request URL: http://.../?do=cnt.getservice&service=getRoomSet
        
        Parameter Options:
        :param *roomSetID: Numeric value of a Room Set.
        '''
        url = "%s/?do=cnt.getservice&service=getRoomSet" %(self.api.base)
        args = {"roomSetID":roomSetID}
        result = self.get_result(url,args)
        # Note to developer - couldn't test this either, data structure might be equivalent
        # with result in result['roomSet'], in which case you can do parse_item(result,'roomSet')
        return ordered_to_dict(result)

    def getRoomsetSearchOptions(self):
        '''getRoomSetSearchOptions
        Returns an XML payload containing search options for the getRoomSetSearchResults service. The
        results of this call are used to obtain valid search values which can be passed to the
        'getRoomSetSearchResults' request.
        Sample Request URL: http://.../?do=cnt.getservice&service=getRoomSetSearchOptions
        Sample XML Payload: See REST_ getRoomSetSearchOptions.xml
        '''
        url = "%s/?do=cnt.getservice&service=getRoomSetSearchOptions" %(self.api.base)
        result = self.get_result(url)
        return ordered_to_dict(result)


    def getRoomSetSearchResults(self,searchText=None,locationID=None,roomID=None,startsOnDate=None,
                                     code=None,postFlag=None):
        '''getRoomSetSearchResults
        Returns an XML payload containing a Room Set listing. This data set returned is smaller than the
        getRoomSets request and intend for listing results. Use the result in combination with the getRoomSet
        call to pull addition information on a specific RoomSet.
        Sample Request URL: http://.../?do=cnt.getservice&service=getRoomSetSearchResults
        
        Request Parameters        
        :param searchText: Text string used to perform a general search of the Room Sets. Searches for matches in
        function name, code, location, and room. 
        :param locationID: Numeric value containing a valid locationID.
        Use the 'getRoomSetSearchOptions' call to obtain a valid list of locations
        :param roomID: Numeric value containing a valid roomID. Use the 'getRoomSetSearchOptions' call to obtain
        a valid list of rooms. 
        :param startsOnDate: Date value containing a valid date. Use the 'getSearchOptions'
        call to obtain a valid list of dates. 
        :param code: text value containing a valid code. Use the 'getSearchOptions' call to obtain the list of possible  
        Room Set Codes.
        :param postFlag: Boolean value (0 or 1).
        '''
        url = "%s/?do=cnt.getservice&service=getRoomSetSearchResults" %(self.api.base)

        args = {"searchText":searchText,
                "locationID":locationID,
                "roomID":roomID,
                "startsOnDate":startsOnDate,
                "code":code,
                "postFlag":postFlag}

        result = self.get_result(url,args)
        return ordered_to_dict(result)
