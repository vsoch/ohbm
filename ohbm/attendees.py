'''
attendees: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items, capitalize

class Attendees():

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
 

    def getSpeakers(self,isScheduledFor,includeActiveStatus,formIDs,modifiedOnAfter,modifiedOnBefore):
        '''getSpeakers
        Returns an XML payload containing a full listing of all speaker data. Speakers are defined as attendees
        whom are participating in the meeting in a specific capacity. E.g. Presenting in a session or
        Moderating a session or Presenting a Poster. This service also returns the schedule for each speaker.
        This includes all itinerary items that are 'active' (can be changed via includeActiveStatus parameter),
        and 'public'.
        Sample Request URL: http://.../?do=cnt.getservice&service=getSpeakers

        Parameter Options:
        :param isScheduledFor: Numeric value of (1,2 or 3) - This filters the speakers returned by schedule type:
        Valid values; 1 = For Event, 2 = For Abstract, 3 = For Event OR Abstract. Note that this parameter
        only affects whether or not a speaker record is included in the results set. It does not change the
        itinerary items that are returned in each speaker's schedule block. For example, if isScheduledFor=2,
        Any speaker who is linked to at least 1 Abstract will be shown. Any 'active', and 'public' itinerary
        items that are linked to an Event will still be shown in the schedule for this speaker.
        :param includeActiveStatus: Numeric value of (0,1, or 99) - Determines if active, inactive, or ALL itinerary
        items are shown in the <schedule> block.
        :param formIDs: Comma delimited list of form ids
        :param modifiedOnAfter: Valid date string. Using this filter will return speakers who have updated contact
        information, schedule, or form responses after/on this date.
        :param modifiedOnBefore: Valid date string. Using this filter will return speakers who have updated contact
        information, schedule, or form responses before/on this date.
        '''
        url = "%s/?do=cnt.getservice&service=getSpeakers" %(self.api.base)
        args = {"isScheduledFor":isScheduledFor,
                "includeActiveStatus":includeActiveStatus,
                "formIDs":formIDs,
                "modifiedOnAfter":modifiedOnAfter,
                "modifiedOnBefore":modifiedOnBefore}

        result = self.get_result(url,args)
        return parse_items(result,'speaker')


    def getSpeaker(self,speakerID,isScheduledFor,formIDs):
        '''getSpeaker
        Returns an XML payload containing a full listing of one speaker. Speaker data consists of their contact
        information, bio and photo. Note Photo's are returned as a url to the actual photo. This service also
        returns the schedule for the speaker. This includes all itinerary items that are 'active' (can be changed
        via includeActiveStatus parameter), and 'public'.
        Sample Request URL: http://.../?do=cnt.getservice&service=getSpeaker
        
        Parameter Options:
        :param *speakerID: Numeric value of a speaker.
        includeActiveStatus: Numeric value of (0,1, or 99) - Determines if active, inactive, or ALL itinerary
        items are shown in the <schedule> block.
        :param isScheduledFor: Numeric value of (1,2 or 3) - This filters the speakers returned by schedule type:
        Valid values; 1 = For Event, 2 = For Abstract, 3 = For Event OR Abstract. Note that this parameter
        only affects whether or not a speaker record is included in the results set. It does not change the
        itinerary items that are returned in each speaker's schedule block. For example, if isScheduledFor=2,
        Any speaker who is linked to at least 1 Abstract will be shown. Any 'active', and 'public' itinerary
        items that are linked to an Event will still be shown in the schedule for this speaker.
        :param formIDs: Comma delimited list of form ids
        '''
        url = "%s/?do=cnt.getservice&service=getSpeaker" %(self.api.base)
        args = {"speakerID":speakerID,
                "isScheduledFor":isScheduledFor,
                "formIDs":formIDs}

        result = self.get_result(url,args)
        return parse_item(result,'speaker')


    def getAttendeesRegData(self,attendeeID=None,startInitial=None,endInitial=None,formID=None):
        '''getAttendeesRegData
        Returns an XML payload containing a full listing of all attendee purchases. For each attendee their
        purchase or order history will be returned in the XML payload. This service is only allowed to be run
        between 11 PM EST and 5 AM EST .
        Sample Request URL: http://.../?do=cnt.getservice&service=getAttendeesRegData
        
        Parameter Options:
        :param attendeeID: Numeric value, Identifies the attendee record to update.
        :param startInitial: 1 character used to indicate the starting initial of the last name range to include. E.g. A
        :param endInitial: 1 character used to indicate the starting initial of the last name range to include. If the
        'startInitial' is provided but no 'endInitial' is provided the system uses the 'startInitial' as the
        'endInitial'. E.g. B
        :param formID: Numeric value of a demographic form
        '''
        url = "%s/?do=cnt.getservice&service=getAttendeesRegData" %(self.api.base)
 
        # Initials should probably always be uppercase
        if startInitial != None:
            startInitial = capitalize(startInitial)
        if endInitial != None:
            endInitial = capitalize(endInitial)

        args = {"attendeeID":attendeeID,
                "startInitial":startInitial,
                "endInitial":endInitial,
                "formID":formID}

        result = self.get_result(url,args)
        return parse_items(result,'attendee')
        

    def getAttendeesItineraryData(self,attendeeID=None,startInitial=None,endInitial=None,insertedInLastHoursSpan=None):
        '''getAttendeesItineraryData
        Returns an XML payload containing a full listing of all attendee itinerary data. For each attendee their
        itinerary will be returned in the XML payload. This service is only allowed to be run between 11 PM
        EST and 5 AM EST. Note: For clients using the Attendee Itinerary Update service, only itinerary
        items with the attributes='ReadWrite' can be modified.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAttendeesItineraryData

        Parameter Options:
        :param attendeeID: Numeric value; Identifies the attendee record to update.
        :param startInitial: 1 character used to indicate the starting initial of the last name range to include. E.g. A
        :param endInitial: 1 character used to indicate the starting initial of the last name range to include. If the
        'startInitial' is provided but no 'endInitial' is provided the system uses the 'startInitial' as the
        'endInitial'. E.g. B
        :param insertedInLastHoursSpan: Used to indicate the number of hour of newly inserted records to include.
        The default is 24. This must be a valid integer between 1 and 26,280.
        '''
        url = "%s/?do=cnt.getservice&service=getAttendeesItineraryData" %(self.api.base)
 
        # Initials should probably always be uppercase
        if startInitial != None:
            startInitial = capitalize(startInitial)
        if endInitial != None:
            endInitial = capitalize(endInitial)

        args = {"attendeeID":attendeeID,
                "startInitial":startInitial,
                "endInitial":endInitial,
                "insertedInLastHoursSpan":insertedInLastHoursSpan}

        result = self.get_result(url,args)
        return parse_items(result,'attendee')


    def getAttendeesFormResponses(self,formID,startInitial=None,endInitial=None):
        '''getAttendeesFormResponses
        Returns an XML payload containing a full listing of attendee contact data and form responses for the
        specified form. For each attendee a 'formResponses' node returned in the XML payload. This service
        is only allowed to be run between 11 PM EST and 5 AM EST.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAttendeesFormResponse
        
        Parameter Options:
        :param *formID: Numeric value; Identifies the form for which to retrieve responses.
        :param attendeeID: Numeric value; Identifies the attendee record to update.
        :param startInitial: 1 character used to indicate the starting initial of the last name range to include. E.g. A
        :param endInitial: 1 character used to indicate the starting initial of the last name range to include. If the
        'startInitial' is provided but no 'endInitial' is provided the system uses the 'startInitial' as the
        'endInitial'. E.g. B
        '''
        # Note to developer - this endpoint has not been tested, was reported wrong in docs
        # https://github.com/vsoch/ohbm/issues/3
        url = "%s/?do=cnt.getservice&service=getAttendeesItineraryData" %(self.api.base)
 
        # Initials should probably always be uppercase
        if startInitial != None:
            startInitial = capitalize(startInitial)
        if endInitial != None:
            endInitial = capitalize(endInitial)

        args = {"formID":formID,
                "startInitial":startInitial,
                "endInitial":endInitial}

        result = self.get_result(url,args)
        return parse_items(result,'attendee')



    def updateItinerary(self,attendeeID,itineraryID,abstractID=None,eventID=None,exhibitorID=None,
                            Description=None,startsOn=None,endsOn=None):
        '''updateItinerary
        Returns an XML payload containing the results of the attendee itinerary data update. The 'stat'
        attribute is used to indicate the success or failure of the request. Extended description of all options are
        listed below.
        Sample Request URL: http://.../?do=cnt.getservice&service=updateItinerary&[Parameter List]

        Parameter Options:
        :param *attendeeID: Identifies the attendee record to update. Always required.
        :param *itineraryID: Identifies the itinerary record to update. Valid options: update, delete; The update option
        is assumed if no action is provided.
        :param abstractID: Identifies the abstract record being added, updated or removed
        :param eventID: Identifies the event record being added, updated or removed
        :param exhibitorID: Identifies the exhibitor record being added, updated or removed title. Title of the activity.
        Limit 300 characters. Required if record is not linked to an event, abstract or exhibitor. If linked to an
        event, abstract or exhibitor, title is ignored.
        :param Description: Description of the event. Limit 500 characters.
        :param startsOn: Date & Time of activity. Format: mm/dd/yyyy hh:mm tt, e.g. 05/01/2011 12:00 PM. Date /
        Time will be ignored if not a valid format or if passed with an event or abstract which already have a
        time associated.
        :param endsOn: Date & Time of activity. Format: mm/dd/yyyy hh:mm tt, e.g. 05/01/2011 12:00 PM. Date /
        Time will be ignored if not a valid format or if passed with an event or abstract which already have a
        time associated.
        '''
        url = "%s/?do=cnt.getservice&service=updateItinerary" %(self.api.base)

        args = {"attendeeID":attendeeID,
                "itineraryID":itineraryID,
                "abstractID":abstractID,
                "eventID":eventID,
                "exhibitorID":exhibitorID,
                "Description":Description,
                "startsOn":startsOn,
                "endsOn":endOn}
 
        result = self.get_result(url,args)
        # Note to developer - I didn't test this because I was nervous about changing itinerary. The response
        # should be tested, and a message to the user returned to verify/deny that the itinerary was changed.
        # It might make sense to have an argument that if True, returns the new itinerary
        return ordered_to_dict(result)


    def addAttendeeActivity(self,attendeeID,registrationNumber=None,eventIDs=None,eventID=None):
        '''addAttendeeActivity
        Returns an XML payload containing the results of the attendee add activity method. The 'stat' attribute
        is used to indicate the success or failure of the request. Extended description of all options are listed
        below.
        Sample Request URL: http://.../?do=cnt.getservice&service=addAttendeeActivity&[Parameter List]
        
        Parameter Options:
        :param *attendeeID: Numeric value used to identify the attendee record to update. attendeeID or
        registrationNumber required.
        :param registrationNumber: String value used to identify the attendee record to update. attendeeID or
        registrationNumber required.
        :param eventIDs: Comma delimited list of event to be added to a person's activity list. eventIDs or eventID
        required
        :param eventID: Numeric value identifying an event to be added to a person's activity list. eventIDs or
        eventID required.
        '''

        if eventIDs == None and eventID == None:
            print("Either eventIDs or eventID must be specified!")
        else:
            url = "%s/?do=cnt.getservice&service=addAttendeeActivity" %(self.api.base)

            args = {"attendeeID":attendeeID,
                    "registrationNumber":registrationNumber,
                    "eventIDs":eventIDs,
                    "eventID":eventID}
 
            result = self.get_result(url,args)
            # Note to developer - ditto above, I didn't test this. The response should be tested and
            # it might make sense to have an argument that if True, returns the new attendee activity
            return ordered_to_dict(result)


    def getPersonActivities(self,attendeeID,lastNameInitialStart=None,lastNameInitialEnd=None):
        '''getPersonActivities
        Returns an XML payload containing the results of the attendee get activity method. The 'stat' attribute
        is used to indicate the success or failure of the request. Extended description of all options are listed
        below.
        Sample Request URL: http://.../?do=cnt.getservice&service=getPersonActivities&[Parameter List]
        
        Parameter Options:
        :param attendeeID: Numeric value; Identifies the attendee record to retrieve.
        :param lastNameInitialStart: 1 character used to indicate the starting initial of the last name range to include.
        E.g. A
        :param lastNameInitialEnd: 1 character used to indicate the starting initial of the last name range to include.
        If the 'lastNameInitialStart' is provided but no 'lastNameInitialEnd' is provided the system uses the
        'lastNameInitialStart' as the 'lastNameInitialEnd'. E.g. B
        '''
        url = "%s/?do=cnt.getservice&service=getPersonActivities" %(self.api.base)
 
        # Initials should probably always be uppercase
        if lastNameInitialStart != None:
            lastNameInitialStart = capitalize(lastNameInitialStart)
        if lastNameInitialEnd != None:
            lastNameInitialEnd = capitalize(lastNameInitialEnd)

        args = {"attendeeID":attendeeID,
                "lastNameInitialStart":lastNameInitialStart,
                "lastNameInitialEnd":lastNameInitialEnd}   

        result = self.get_result(url,args)
        # Note to developer - did not test this call
        return ordered_to_dict(result)


    def getAttendeesCreditActivity(self,attendeeID=None,attendeesID=None,memberNumber=None,memberNumberPartial=None,
                                        lastNameInitialStart=None,lastNameInitialEnd=None,plannerID=None,
                                        claimedOnAfter=None,claimedOnBefore=None):
        '''getAttendeesCreditActivity
        Returns an XML payload containing and attendee(s) data and credit activity grouped by
        planner/activity. Credit activities consist of the claimed activities, the activities' displayed credit, the
        activities' credit types/accreditation bodies (based on the attendee's registration type), and the credit
        awarded for each credit type/accreditation body.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAttendeesCreditActivity&[Parameter
        List]

        Parameter Options:        
        :param attendeeID: Numeric value; Identifies the attendee record to retrieve.
        :param attendeesID: List of numeric values; Identifies attendee records to retrieve.
        :param memberNumber: String value. Identifies the attendee record to retrieve.
        :param memberNumberPartial: String value. Partial member number used to search/identify attendee
        records to retrieve.
        :param lastNameInitialStart: 1 character used to indicate the starting initial of the last name range to include.
        E.g. A. Must be used with lastNameInitialEnd
        :param lastNameInitialEnd: 1 character used to indicate the starting initial of the last name range to include.
        E.g. B. Must be used with lastNameInitialStart
        :param plannerID: Numeric value; Used to filter the activities. Identifies the planner/activity to include.
        :param claimedOnAfter: Date; Used to filter the activities.
        :param claimedOnBefore: Date; Used to filter the activities
        '''
        url = "%s/?do=cnt.getservice&service=getAttendeesCreditActivity" %(self.api.base)
 
        # Initials should probably always be uppercase
        if lastNameInitialStart != None:
            lastNameInitialStart = capitalize(lastNameInitialStart)
        if lastNameInitialEnd != None:
            lastNameInitialEnd = capitalize(lastNameInitialEnd)

        args = {"attendeeID":attendeeID,
                "attendeesID":attendeesID,
                "memberNumber":memberNumber,
                "memberNumberPartial":memberNumberPartial,
                "plannerID":plannerID,
                "claimedOnAfter":claimedOnAfter,
                "claimedOnBefore":claimedOnBefore,
                "lastNameInitialStart":lastNameInitialStart,
                "lastNameInitialEnd":lastNameInitialEnd}   

        result = self.get_result(url,args)
        # Note to developer - did not test this call
        return ordered_to_dict(result)

    def getAttendeesCreditActivitySummary(self,attendeeID=None,attendeesID=None,memberNumber=None,memberNumberPartial=None,
                                               lastNameInitialStart=None,lastNameInitialEnd=None,plannerID=None,
                                               claimedOnAfter=None,claimedOnBefore=None):
        '''getAttendeesCreditActivitySummary
        Returns an XML payload containing and attendee(s) data and credit activity summaries grouped by
        planner/activity. The credit activities summaries consist of the total number of activities, display credits
        sum, awarded credit sum for each credit type/accreditation body.
        Sample Request URL: http://.../?do=cnt.getservice&service=getAttendeesCreditActivitySummary&[Parameter List]

        Parameter Options:
        :param attendeeID: Numeric value; Identifies the attendee record to retrieve.
        :param attendeesID: List of numeric values; Identifies attendee records to retrieve.
        :param memberNumber: String value. Identifies the attendee record to retrieve.
        :param memberNumberPartial: String value. Partial member number used to search/identify attendee
        records to retrieve.
        :param lastNameInitialStart: 1 character used to indicate the starting initial of the last name range to include.
        E.g. A. Must be used with lastNameInitialEnd
        :param lastNameInitialEnd: 1 character used to indicate the starting initial of the last name range to include.
        E.g. B. Must be used with lastNameInitialStart
        :param plannerID: Numeric value; Used to filter the activities. Identifies the planner/activity to include.
        :param claimedOnAfter: Date; Used to filter the activities.
        :param claimedOnBefore: Date; Used to filter the activities
        '''
        url = "%s/?do=cnt.getservice&service=getAttendeesCreditActivitySummary" %(self.api.base)
 
        # Initials should probably always be uppercase
        if lastNameInitialStart != None:
            lastNameInitialStart = capitalize(lastNameInitialStart)
        if lastNameInitialEnd != None:
            lastNameInitialEnd = capitalize(lastNameInitialEnd)

        args = {"attendeeID":attendeeID,
                "attendeesID":attendeesID,
                "memberNumber":memberNumber,
                "memberNumberPartial":memberNumberPartial,
                "plannerID":plannerID,
                "claimedOnAfter":claimedOnAfter,
                "claimedOnBefore":claimedOnBefore,
                "lastNameInitialStart":lastNameInitialStart,
                "lastNameInitialEnd":lastNameInitialEnd}   

        result = self.get_result(url,args)
        # Note to developer - did not test this call either :)
        return ordered_to_dict(result)
