'''
abstracts: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class Abstracts():

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
 

    def getAbstracts(self,categoryID=None,speakerID=None,abstractTypeID=None,acceptedFlag=None):
        '''getAbstracts
        Returns an XML payload containing a full listing of all abstract data. Abstract data consists primarily
        of the title, abstract number, purpose, materials & methods, results & conclusions.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAbstracts

        Parameter Options:
        :param categoryID: Numeric value containing a valid category. Use the 'getSearchOptions' call to obtain a
        valid list of categories
        :param speakerID: Numeric value containing a valid speaker. Use the 'getSearchOptions' call to obtain the
        list of possible speakers.
        :param abstractTypeID: Numeric value containing a valid abstract type. Use the 'getSearchOptions' call to
        obtain the list of possible abstract types.
        :param acceptedFlag: Boolean value (0 or 1). Default is 1.
        '''
        url = "%s/?do=cnt.getservice&service=getAbstracts" %(self.api.base)
        args = {"categoryID":categoryID,
                "speakerID":speakerID,
                "abstractTypeID":abstractTypeID,
                "acceptedFlag":acceptedFlag}

        result = self.get_result(url,args)
        return parse_items(result,'abstract')


    def getAbstract(self,abstractID):
        '''getAbstract
        Returns an XML payload containing a full listing of one abstract. Abstract data consists primarily of
        the title, abstract number, purpose, materials & methods, results & conclusions. Note: The result set
        provides urls to the figures or documents which are actual files.        
        Sample Request URL: http://.../?do=cnt.getservice&service=getAbstract

        Parameter Options:
        :param *abstractID: Numeric value of an abstract.
        Sample XML Payload: See REST_getAbstract.xml
        '''
        url = "%s/?do=cnt.getservice&service=getAbstract" %(self.api.base)
        args = {"abstractID":abstractID}
        result = self.get_result(url,args)
        return parse_item(result,'abstract')

    def getAbstractSearchOptions(self):
        '''getAbstractSearchOptions
        Returns an XML payload containing search options for the getAbstractSearchResults service. The
        results of this call are used to obtain valid search values which can be passed to the
        'getAbstractSearchResults' request.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAbstractSearchOptions
        '''
        url = "%s/?do=cnt.getservice&service=getAbstractSearchOptions" %(self.api.base)
        result = self.get_result(url)
        return ordered_to_dict(result)


    def getAbstractSearchResults(self,searchText,categoryID=None,speakerID=None,abstractTypeID=None):
        '''getAbstractSearchResults
        Returns an XML payload containing an abstract listing. This data set returned is smaller than the
        getAbstracts request and intend for listing results. Use the result in combination with the getAbstract
        call to pull addition information on a specific abstract.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAbstractSearchResults

        Parameter Options:
        :param *searchText: Text string used to perform a general search of the events. This parameter is used to find
        matches in the title, description, objectives or speaker names.
        :param categoryID: Numeric value containing a valid category. Use the 'getSearchOptions' call to obtain a
        valid list of categories
        :param speakerID: Numeric value containing a valid speaker. Use the 'getSearchOptions' call to obtain the
        list of possible speakers.
        :param abstractTypeID: Numeric value containing a valid abstract type. Use the 'getSearchOptions' call to
        obtain the list of possible abstract types. acceptedFlag: Boolean value (0 or 1). Default is 1.
        '''
        url = "%s/?do=cnt.getservice&service=getAbstractSearchResults" %(self.api.base)
        args = {"searchText":searchText,
                "categoryID":categoryID,
                "speakerID":speakerID,
                "abstractTypeID":abstractTypeID}

        result = self.get_result(url,args)
        return parse_items(result,'abstract')
