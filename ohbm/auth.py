'''
auth: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class Authenticate():

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


    def authenticateBase(self,url,username,password):
        '''a general function for authenticating, and returning result
        :param *url: the URL to send the request to
        :param *username: the username
        :param *password: the password
        '''
        args = {"username":username,
                "password":password}

        result = self.get_result(url,args)
        if 'authentication' in result:
            result = result['authentication']
            if "@result" in result:
                print("Credentials are %s" %(result['@result']))
    
        return ordered_to_dict(result)

 
    def authenticatePerson(self,username,password):
        '''authenticatePerson
        Returns an XML payload used to indicate if the sign in credentials provided are valid. When valid
        credentials are provided the XML payload will return the person's first name, last name, company and
        email.
        Sample Request URL: http://.../?do=cnt.getservice&service=authenticatePerson

        Parameter Options:
        :param *username: Text string of the person's username
        :param *password: Text string of the person's password
        '''
        url = "%s/?do=cnt.getservice&service=authenticatePerson" %(self.api.base)
        return self.authenticateBase(url,username,password)


    def authenticateCompany(self,username,password):
        '''authenticateCompany
        Returns an XML payload used to indicate if the sign in credentials provided are valid. When valid
        credentials are provided the XML payload will return the company contact's first name, last name,
        company and email.
        Sample Request URL: http://.../?do=cnt.getservice&service=authenticateCompany

        Parameter Options:
        :param *username: Text string of the person's username
        :param *password: Text string of the person's password
        '''
        url = "%s/?do=cnt.getservice&service=authenticateCompany" %(self.api.base)
        return self.authenticateBase(url,username,password)


    def authenticateVendor(self,username,password):
        '''authenticateVendor
        Returns an XML payload used to indicate if the sign in credentials provided are valid. When valid
        credentials are provided the XML payload will return the vendor company and email.
        Sample Request URL: http://.../?do=cnt.getservice&service=authenticateVendor

        Parameter Options:
        :param *username: Text string of the person's username
        :param *password: Text string of the person's password
        '''
        url = "%s/?do=cnt.getservice&service=authenticateVendor" %(self.api.base)
        return self.authenticateBase(url,username,password)

