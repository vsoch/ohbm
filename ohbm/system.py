'''
system: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class System():

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


    def getEventTypes(self,eventType=None):
        '''getEventTypes
        Returns an XML payload containing a listing of event types. Event type data contains the type name
        and roles that may be assigned to an event of this type.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventTypes

        Parameter Options:
        :param eventType: Integer valid values: 1= Event, 2=Abstract
        If not provided the system defaults to sending Event roles.
        '''
        url = "%s/?do=cnt.getservice&service=getEventTypes" %(self.api.base)
        args = {"type":eventType}
        result = self.get_result(url,args)
        return parse_items(result,'eventType')


    def getForm(self,formID):
        '''getForm
        Returns an XML payload containing form data. Form data includes form settings, questions and
        answers.
        Sample Request URL: http://.../?do=cnt.getservice&service=getForm

        Parameter Options:
        :param *formID: Numeric value containing a valid form ID.
        '''
        url = "%s/?do=cnt.getservice&service=getForm" %(self.api.base)
        args = {"formID":formID}
        result = self.get_result(url,args)
        return ordered_to_dict(result)


    def getLocations(self):
        '''getLocations
        Returns an XML payload containing a full listing of location and room data.
        Sample Request URL: http://.../?do=cnt.getservice&service=getLocations        
        '''
        url = "%s/?do=cnt.getservice&service=getLocations" %(self.api.base)
        result = self.get_result(url)
        return parse_items(result,'location')
        

    def getPublicFields(self,eventType=None):
        '''getPublicFields
        Returns an XML payload containing public fields for one of the following: Event, Exhibitor, Abstract,
        Speaker. Field data will contain the field ID and public label.
        Sample Request URL: http://.../?do=cnt.getservice&service=getPublicFields

        Parameter Options:
        :param eventType: Integer valid values: 1= Event, 2=Exhibitor, 3=Abstract & 4=Speaker
        If not provided the system defaults to sending Event fields.
        '''
        url = "%s/?do=cnt.getservice&service=getPublicFields" %(self.api.base)
        args = {"type":eventType}
        result = self.get_result(url,args)
        return parse_items(result,'field')


    def getScheduledRoles(self,eventType=None):
        '''getScheduledRoles
        Returns an XML payload containing roles used by Events or Abstracts. Role data will contain the role
        name, type, and public label.
        Sample Request URL: http://.../?do=cnt.getservice&service=getScheduledRoles
        :param eventType: Integer valid values: 1= Event, 2=Abstract
        If not provided the system defaults to sending Event roles.
        '''
        url = "%s/?do=cnt.getservice&service=getScheduledRoles" %(self.api.base)
        args = {"type":eventType}
        result = self.get_result(url,args)
        return parse_items(result,'role')

    def getRegistrationTypes(self):
        '''getRegistrationTypes
        Returns an XML payload containing registration type data. Registration type data will contain the
        registration type name, code, description, and evaluation links. Note: The tag, AI_ATTENDEEID, may
        be used within data elements and serves as a placeholder to be replaced by a valid attendee ID. The tag,
        AI_EVENTID, may be used within data elements and serves as a placeholder to be replaced by a valid
        event ID.
        Sample Request URL: http://.../?do=cnt.getservice&service=getRegistrationTypes
        '''
        url = "%s/?do=cnt.getservice&service=getRegistrationTypes" %(self.api.base)
        result = self.get_result(url)
        return parse_items(result,'registrationType')


    def getMenu(self,menuID):
        '''getMenu
        Returns an XML payload containing a menu item and its content pages.
        Sample Request URL: http://.../?do=cnt.getservice&service=getMenu&[parameters list]
        
        Parameter Options:
        :param *menuID: Numeric value containing a valid menu id.
        '''
        url = "%s/?do=cnt.getservice&service=getMenu" %(self.api.base)
        args = {"menuID":menuID}
        result = self.get_result(url,args)
        # Note to developer - not tested, result is likely in some format like result['menus']['menu'] and
        # you could use parse_items(result,'menu')
        return ordered_to_dict(result)


    def getMeetingTimes(self):
        '''getMeetingTimes
        Returns an XML payload containing a listing of all active meeting times/time ranges.
        Sample Request URL: http://.../?do=cnt.getservice&service=getMeetingTimes
        '''
        url = "%s/?do=cnt.getservice&service=getMeetingTimes" %(self.api.base)
        result = self.get_result(url)
        return parse_items(result,'meetingTime')

    def getMeetingTime(self,meetingTimeID):
        '''getMeetingTime
        Returns an XML payload containing a meeting time/time range. This payload includes the meeting
        time's type, code, name, description, and start and end date.
        Sample Request URL: http://.../?do=cnt.getservice&service=getMeetingTime

        Parameter Options:
        :param meetingTimeID: Numeric value containing a valid meeting time id.
        '''
        url = "%s/?do=cnt.getservice&service=getMeetingTime" %(self.api.base)
        args = {"meetingTimeID":meetingTimeID}
        result = self.get_result(url,args)
        return parse_item(result,'meetingTime')
