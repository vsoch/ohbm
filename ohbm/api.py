'''
api: part of the ohbm-api
A wrapper for all python modules, for user to explore dynamically
This can (eventually) be useful if more fine tune control is needed
for giving different kinds of users access to modules. For now, all
are exposed.

@vsoch 7/23/2016

'''

from ohbm.settings import access_token, base #for development only
from ohbm.utils import get_result, ordered_to_dict
from pokemon.skills import get_avatar

# Imports for different function classes
from ohbm.categories import Categories
from ohbm.exhibitors import Exhibitor
from ohbm.abstracts import Abstracts
from ohbm.attendees import Attendees
from ohbm.auth import Authenticate
from ohbm.roomset import Roomset
from ohbm.planner import Planner
from ohbm.system import System
from ohbm.events import Events

# Third party
import tempfile
import shutil
import numpy
import stat
import uuid
import json
import sys
import os
import re

class Api():

    def __init__(self,access_token=None,base_url=None):

        # For development only - should return error without one.
        if access_token == None:
            self.key = access_token
        else:
            self.key = access_token

        # Alert the user we are good, show pokemon avatar
        get_avatar(access_token,include_name=False)
        print("\nWelcome, OHBM Trainer!")

        if base_url == None:
            self.base = base
        else:
            self.base = base_url

        # Instantiate each class
        #self.Abstracts = Abstracts(api=self)
        #self.Attendees = Attendees(api=self)
        #self.Authenticate = Authenticate(api=self)
        self.Categories = Categories(api=self)
        self.Events = Events(api=self)
        #self.Exhibitor = Exhibitor(api=self)
        #self.Planner = Planner(api=self)
        #self.Roomset = Roomset(api=self)
        #self.System = System(api=self)
