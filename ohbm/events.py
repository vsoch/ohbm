'''
events: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class Events():

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
        

    def getEvents(self,statusFlag=None,publicUseFlag=None,approvedFlag=None,
                       categoryID=None,plannerID=None,startsOnDate=None):
        '''Returns an XML payload containing a full listing of all event or session data. Event or session data 
        consists primarily of the name, date, time description and location of events. Note: the tag,
        AI_ATTENDEEID, may be used within data elements and serves as a placeholder to be replaced by a
        valid attendee ID. This method is only available in its entirety between 7PM and 7AM. Between 7AM and 7PM the
        method will at most 5 event entries.

        :param statusFlag: Valid values: 1-Active; 0-Inactive; -1-All; Used to indicate if the event is active or
        inactive. Generally inactive events are events that have been cancelled or removed by the client.
        :param publicUseFlag: Valid values: 1=Public; 0=Private; -1=All; Used to determine the types of events to
        include. Public events are viewable to the general population. Private events are events clients are
        witholding from the general viewing public
        :param approvedFlag: Valid values: 1=Approved; 0=Not Approved; -1=Both; Used to determine the types of
        events to include. Note that a site setting can be used to use approvedFlag=1 by default. However,
        passing the parameter via the url will override the site setting parameter.
        :param categoryID: Numeric value; Use the 'getCategories' REST call to pull a list of valid categories.
        :param plannerID: Numeric value containing a valid planner.
        :param startsOnDate: Date value containing a valid date. Use the 'getSearchOptions' call to obtain a valid list
        of dates.
        '''
        url = "%s/?do=cnt.getservice&service=getEvents" %(self.api.base)
        args = {"statusFlag":statusFlag,
                "publicUseFlag":publicUseFlag,
                "approvedFlag":approvedFlag,
                "categoryID":categoryID,
                "plannerID":plannerID,
                "startsOnDate":startsOnDate}

        result = self.get_result(url,args)
        return parse_items(result,"event")


    def getEvent(self,eventID):
        '''Returns an XML payload containing the details of a single event.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEvent
        Parameter Options:
        :param apiKey: Valid API key
        :param eventID: Numeric value of an event.
        '''
        url = "%s/?do=cnt.getservice&service=getEvent" %(self.api.base)
        args = {"eventID":eventID}

        result = self.get_result(url,args)
        return parse_item(result,"event")


    def getEventSearchOptions(self):
        '''getEventSearchOptions returns an XML payload containing search options for the getSearchResults service. The  
        results of this call are used to obtain valid search values which can be passed to the 'getSearchResults' request.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventSearchOptions
        '''
        url = "%s/?do=cnt.getservice&service=getEventSearchOptions" %(self.api.base)
        result = self.get_result(url)
        return ordered_to_dict(result)


    def getEventSearchResults(self,searchText=None,categoryID=None,locationID=None,speakerID=None,
                                   startsOnDate=None,startsOnTime=None,statusFlag=None):
        '''getEventSearchResults
        Returns an XML payload containing an event listing. This data set returned is smaller than the
        getEvents request and intend for listing results. Use the result in combination with the getEvent call to
        pull addition information on a specific event.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventSearchResults
        
        Parameter Options:
        :param searchText: Text string used to perform a general search of the events. This parameter is used to find
        matches in the title, description, objectives or speaker names.
        :param categoryID: Numeric value containing a valid category. Use the 'getSearchOptions' call to obtain a
        valid list of categories
        :param locationID: Numeric value containing a valid location. Use the 'getSearchOptions' call to obtain a
        valid list of locations
        :param speakerID: Numeric value containing a valid speaker. Use the 'getSearchOptions' call to obtain the
        list of possible speakers.
        :param startsOnDate: Date value containing a valid date. Use the 'getSearchOptions' call to obtain a valid list
        of dates.
        :param startsOnTime: Time value in 12 hour format. E.g. 6:30PM
        :param statusFlag: Valid values: 1-Active; 0-Inactive; -1-All; Used to indicate if the event is active or
        inactive. Generally inactive events are events that have been cancelled or removed by the client.
        '''
        url = "%s/?do=cnt.getservice&service=getEventSearchResults" %(self.api.base)
        
        args = {"searchText":searchText,
                "categoryID":categoryID,
                "locationID":locationID,
                "speakerID":speakerID,
                "startsOnDate":startsOnDate,
                "startsOnTime":startsOnTime,
                "statusFlag":statusFlag}

        result = self.get_result(url,args)
        return parse_items(result,"event")


    def getEventsCreditsSummary(self,statusFlag=None,publicUseFlag=None,approvedFlag=None,
                                     categoryID=None,plannerID=None,startsOnDate=None):
        '''getEventsCreditsSummary
        Returns an XML payload containing a full listing of event or session credit data. Event or session data
        consists primarily of the name, date, time description and location of events. Credit data primarily
        consists of the total credits claimed and people who have claimed those credits. Note: The tag,
        AI_ATTENDEEID, may be used within data elements and serves as a placeholder to be replaced by a
        valid attendee ID.
        This method is only available in its entirety between 7PM and 7AM. Between 7AM and 7PM the
        method will at most 5 event entries.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventsCreditsSummary
        
        Parameter Options:
        :param statusFlag: Valid values: 1-Active; 0-Inactive; -1-All; Used to indicate if the event is active or
        inactive. Generally inactive events are events that have been cancelled or removed by the client.
        :param publicUseFlag: Valid values: 1=Public; 0=Private; -1=All; Used to determine the types of events to
        include. Public events are viewable to the general population. Private events are events clients are
        withholding from the general viewing public
        :param approvedFlag: Valid values: 1=Approved; 0=Not Approved; -1=Both; Used to determine the types of
        events to include. Note that a site setting can be used to use approvedFlag=1 by default. However,
        passing the parameter via the url will override the site setting parameter.
        :param categoryID: Numeric value; Use the 'getCategories' REST call to pull a list of valid categories.
        :param plannerID: Numeric value containing a valid planner.
        :param startsOnDate: Date value containing a valid date. Use the 'getSearchOptions' call to obtain a valid list
of dates.
        '''
        url = "%s/?do=cnt.getservice&service=getEventsCreditsSummary" %(self.api.base)
        
        args = {"statusFlag":statusFlag,
                "publicUseFlag":publicUseFlag,
                "approvedFlag":approvedFlag,
                "categoryID":categoryID,
                "plannerID":plannerID,
                "startsOnDate":startsOnDate}

        result = self.get_result(url,args)
        return parse_items(result,"event")


    def getEventCreditSummary(self,eventID):
        '''getEventCreditsSummary
        Returns an XML payload containing the credit details of a single event.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventCreditsSummary
        Parameter Options:
        :param *eventID: Numeric value of an event.
        '''
        url = "%s/?do=cnt.getservice&service=getEventCreditsSummary" %(self.api.base)
        args = {"eventID":eventID}
        result = self.get_result(url,args)
        return parse_item(result,"event")


    def getEventsCreditsByRegTypeSummary(self,statusFlag=None,publicUseFlag=None,approvedFlag=None,
                                              categoryID=None,plannerID=None):
        '''service=getEventsCreditsByRegTypeSummary
        Returns an XML payload containing a full listing of event or session credit data grouped by registration
        type. Event or session data consists primarily of the name, date, time description and location of
        events. Credit data primarily consists of the total credits claimed and people who have claimed those
        credits. Note: The tag, AI_ATTENDEEID, may be used within data elements and serves as a
        placeholder to be replaced by a valid attendee ID. The data excludes people who do not have a
        registration type.

        This method is only available in its entirety between 7PM and 7AM. Between 7AM and 7PM the
        method will at most 5 event entries.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventsCreditsByRegTypeSummary

        Parameter Options:
        :param statusFlag: Valid values: 1-Active; 0-Inactive; -1-All; Used to indicate if the event is active or
        inactive. Generally inactive events are events that have been cancelled or removed by the client.
        :param publicUseFlag: Valid values: 1=Public; 0=Private; -1=All; Used to determine the types of events to
        include. Public events are viewable to the general population. Private events are events clients are
        withholding from the general viewing public
        :param approvedFlag: Valid values: 1=Approved; 0=Not Approved; -1=Both; Used to determine the types of
        events to include. Note that a site setting can be used to use approvedFlag=1 by default. However,
        passing the parameter via the url will override the site setting parameter.
        :param categoryID: Numeric value; Use the 'getCategories' REST call to pull a list of valid categories.
        :param plannerID: Numeric value containing a valid planner. startsOnDate: Date value containing a valid
        date. Use the 'getSearchOptions' call to obtain a valid list of dates.
        '''
        url = "%s/?do=cnt.getservice&service=getEventsCreditsByRegTypeSummary" %(self.api.base)

        args = {"statusFlag":statusFlag,
                "publicUseFlag":publicUseFlag,
                "approvedFlag":approvedFlag,
                "categoryID":categoryID,
                "plannerID":plannerID}

        result = self.get_result(url,args)
        return parse_items(result,"event")


    def getEventCreditsByRegTypeSummary(self,eventID):
        '''getEventCreditsByRegTypeSummary
        Returns an XML payload containing the credit details grouped by registration type of a single event.
        Sample Request URL: http://.../?do=cnt.getservice&service=getEventCreditsByRegTypeSummary
        Parameter Options:
        :param *apiKey: Valid API key
        :param *eventID: Numeric value of an event.
        '''
        url = "%s/?do=cnt.getservice&service=getEventCreditsByRegTypeSummary" %(self.api.base)
        args = {"eventID":eventID}
        result = self.get_result(url,args)
        return parse_item(result,"event")
        
