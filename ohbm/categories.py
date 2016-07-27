'''
categories: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict

class Categories():

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

 
    def getCategories(self,categoryTypeID=None,includeAdminOnlyCategories=None):
        '''getCategories
        Returns an XML payload containing a full listing of all category data. Category data consists primarily
        of the category name and sub-categories.
        Sample Request URL: http://.../?do=cnt.getservice&service=getCategories
        
        Parameter Options:
        :param categoryTypeID: Integer valid values: 1= Event, 2=Exhibitor & 3=Abstract If
        not provided the system defaults to sending Event categories.
        :param includeAdminOnlyCategories: 0 or 1 (represents true or false).
        '''
        url = "%s/?do=cnt.getservice&service=getCategories" %(self.api.base)

        args = {"categoryTypeID":categoryTypeID,
                "includeAdminOnlyCategories":includeAdminOnlyCategories}

        result = self.get_result(url,args)
        if "categories" in result:
            if "category" in result['categories']:
                result = result["categories"]["category"]
                print("Found %s categories!" %(len(result)))
        return ordered_to_dict(result)

