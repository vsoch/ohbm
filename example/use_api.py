#!/usr/bin/python

from ohbm.api import Api

access_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
api = Api(access_token)

# Retrieve all abstracts
abstracts = api.Abstracts.getAbstracts()
