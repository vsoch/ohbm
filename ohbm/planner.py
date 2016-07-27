'''
planner: part of the ohbm-api

'''

from ohbm.utils import get_url, ordered_to_dict, parse_item, parse_items

class Planner():

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
 

    def getActivities(self,plannerID=None,activityID=None,startsOn=None,startsOnOrAfter=None,startsOnOrBefore=None,
                           insertedOn=None,insertedOnOrAfter=None,insertedOnOrBefore=None):
        '''getActivities
        Returns an XML payload containing activity details. This payload includes the activity's title, codes,
        start/end dates, description, location, and ACCME PARS information. This payload also contains a
        listing of the activity's public role assignments.
        Sample Request URL: http://.../?do=cnt.getservice&service=getActivities

        Parameter Options:
        :param plannerID: Numeric identifier for a valid planner. Use this parameter to request the details of a single
        planner.
        :param activityID: Numeric identifier for a valid activity. Use this this parameter to request the details of a
        single activity.
        :param startsOn: Date value containing a valid date. Use this parameter to request the details of any activity
        that begins on this date.
        :param startsOnOrAfter: Date value containing a valid date. Use this parameter to request the details of any
        activity that begins on or after this date.
        :param startsOnOrBefore: Date value containing a valid date. Use this parameter to request the details of any
        activity that begins on or before this date.
        :param insertedOn: Date value containing a valid date. Use this parameter to request the details of any activity
        that was added to the system on this date.
        :param insertedOnOrAfter: Date value containing a valid date. Use this parameter to request the details of
        any activity that was added to the system on or after this date.
        :param insertedOnOrBefore: Date value containing a valid date. Use this parameter to request the details of
        any activity that was added to the system on or before this date.
        '''

        url = "%s/?do=cnt.getservice&service=getActivities" %(self.api.base)
        args = {"plannerID":plannerID,
                "activityID":activityID,
                "startsOn":startsOn,
                "startsOnOrAfter":startsOnOrAfter,
                "startsOnOrBefore":startsOnOrBefore,
                "insertedOn":insertedOn, 
                "insertedOnOrAfter":insertedOnOrAfter,
                "insertedOnOrBefore":insertedOnOrBefore}

        result = self.get_result(url,args)
        # Note to developer - in testing, I would have assumed that a call without any args would return all
        # activities - the result was empty. This is either not developed, or a bug, so the result here is not 
        # parse in any way.
        return ordered_to_dict(result)


    def getActivity(self,plannerID,activityID):
        '''getActivity
        Returns an XML payload containing an activity's details. This payload includes the activity's title,
        codes, start/end dates, description, location, and ACCME PARS information. This payload also
        contains a listing of the activity's public role assignments and event (if the activity is one-to-one)
        Sample Request URL: http://.../?do=cnt.getservice&service=getActivity

        Parameter Options:
        :param *plannerID: Numeric identifier for a valid planner. Use this parameter to request the details of a single
        planner.
        :param *activityID: Numeric identifier for a valid activity. Use this this parameter to request the details of a
        single activity.
        '''
        url = "%s/?do=cnt.getservice&service=getActivity" %(self.api.base)

        args = {"plannerID":plannerID,
                "activityID":activityID}

        result = self.get_result(url,args)
        # Note to developer - same issue here, not sure about the format this will be returned in, so returning raw
        return ordered_to_dict(result)
