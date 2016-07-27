'''
api: part of the ohbm-api
A wrapper for all python modules, for user to explore dynamically
This can (eventually) be useful if more fine tune control is needed
for giving different kinds of users access to modules. For now, all
are exposed.

@vsoch 7/23/2016

'''

from ohbm.settings import access_token, base #for development only
from pokemon.skills import get_avatar, get_ascii

# Imports for different function classes
from ohbm.categories import Categories
from ohbm.exhibitor import Exhibitor
from ohbm.abstracts import Abstracts
from ohbm.attendees import Attendees
from ohbm.auth import Authenticate
from ohbm.roomset import Roomset
from ohbm.planner import Planner
from ohbm.system import System
from ohbm.events import Events

import sys

# Base URL, likely for testing
base = "https://ww5.aievolution.com/hbm1601"

class Api():

    def __init__(self,access_token=None):

        # For development only - should return error without one.
        if access_token == None:
            message="Please specify an access_token!"
            get_ascii(name="charmander",message=message)
            sys.exit(1)
        else:
            self.key = access_token

        # Alert the user we are good, show pokemon avatar
        get_avatar(access_token,include_name=False)
        print("\nWelcome, OHBM Trainer!")
        self.base = base

        # Instantiate each class
        self.Abstracts = Abstracts(api=self)
        self.Attendees = Attendees(api=self)
        self.Authenticate = Authenticate(api=self)
        self.Categories = Categories(api=self)
        self.Events = Events(api=self)
        self.Exhibitor = Exhibitor(api=self)
        self.Planner = Planner(api=self)
        self.Roomset = Roomset(api=self)
        self.System = System(api=self)
