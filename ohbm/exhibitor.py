'''
exhibitor: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class Exhibitor():

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
 

    def getExhibitors(self):
        '''service=getExhibitors
        Returns an XML payload containing a full listing of all exhibitor data. Exhibitor data consists
        primarily of the company name, address and contact information.
        Sample Request URL: http://.../?do=cnt.getservice&service=getExhibitors

        Parameter Options:
        :param apiKey: Valid API key
        '''
        url = "%s/?do=cnt.getservice&service=getExhibitors" %(self.api.base)
        result = self.get_result(url)
        return parse_items(result,'exhibitor')


    def getExhibitor(self,exhibitorID):
        '''getExhibitor
        Returns an XML payload containing a full listing of one exhibitor. Exhibitor data consists primarily of
        the company name, address and contact information.
        Sample Request URL: http://.../?do=cnt.getservice&service=getExhibitor

        Parameter Options:
        :param *exhibitorID: Numeric value of an exhibitor
        '''
        url = "%s/?do=cnt.getservice&service=getExhibitor" %(self.api.base)
        args = {"exhibitorID":exhibitorID}
        result = self.get_result(url,args)
        # Note to developer - this is assuming the structure of these results is akin to the events,
        # like result['exhibitors']['exhibitor']
        return parse_item(result,'exhibitor')


    def getExhibitorSearchOptions(self):
        '''getExhibitorSearchOptions
        Returns an XML payload containing search options for the getExhibitorSearchResults service. The
        results of this call are used to obtain valid search values which can be passed to the
        'getExhibitorSearchResults' request.
        Sample Request URL: http://.../?do=cnt.getservice&service=getExhibitorSearchOptions
        Sample XML Payload: See REST_getExhibitorSearchOptions.xml
        '''
        url = "%s/?do=cnt.getservice&service=getExhibitorSearchOptions" %(self.api.base)
        result = self.get_result(url)
        # Note to developer - this call seems to return a structure that has "categories" - this
        # might be a bug in the base API
        # See https://github.com/vsoch/ohbm/issues/1
        return ordered_to_dict(result)


    def getExhibitorSearchResults(self,searchText=None,categoryID=None):
        '''getExhibitorSearchResults
        Returns an XML payload containing an exhibitor listing. This data set returned is smaller than the
        getExhibitors request and intend for listing results. Use the result in combination with the getExhibitor
        call to pull addition information on a specific event.
        Sample Request URL: http://.../?do=cnt.getservice&service=getExhibitorSearchResults

        Parameter Options:

        :param searchText: Text string used to perform a general search of the events. This parameter is used to find
        param matches in the title, description, objectives or speaker names.
        :param categoryID: Numeric value containing a valid category. Use the 'getSearchOptions' call to obtain a
        valid list of categories
        '''
        url = "%s/?do=cnt.getservice&service=getExhibitorSearchResults" %(self.api.base)

        args = {"searchText":searchText,
                "categoryID":categoryID}
        result = self.get_result(url,args)
        # Note to developer - I wasn't able to get any results for these queries, so I'm not sure what
        # they are supposed to look like. If the structure is result['exhibitors']['exhibitor'] then the parse_items
        # function could handle like parse_items(result,'exhibitor')
        return ordered_to_dict(result)

