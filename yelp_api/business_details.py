import argparse
import json
import pprint
import requests
import sys
import urllib

#TODO: generate new API key for use in production website
API_KEY= 'zd2uwmgCgOAh4tq7X4XlO6Otfk64uUIPRjk3S6-aLK2U98pJdD27bPslfqNtV_Z5FYrGmsO9xvq65DMUHpOvDk8700Fwon4_vZImf7riM2kofgYdeut1zZtiXhO6WnYx'


# API constants, we shouldn't have to change these...
# unless we need different paths, but we can just add more here, like transactions
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# Defaults
DEFAULT_TERM = 'lunch'
DEFAULT_LOCATION = 'Dublin, IE'
SEARCH_LIMIT = 3
