# -*- coding: utf-8 -*-
# based on https://raw.githubusercontent.com/pyeve/eve-demo/master/settings.py settings file
# http://python-eve.org/config.html

"""
    sms api settings
    ~~~~~~~~~~~~~~~~~

    Eve Settings file for sms api
"""

from __future__ import absolute_import
import os

# https://stackoverflow.com/questions/33767597/request-items-only-using-python-eve-api-to-a-mongodb
#HATEOAS = False

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'tmp-sms-db')

#URL_PREFIX = 'api'
#API_VERSION = 'v1'

#https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#https://docs.python.org/3.5/library/datetime.html

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
#ITEM_METHODS = ['GET', 'PATCH']
ITEM_METHODS = ['GET']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

SMS = {
    'item_title': 'sms',
    'schema': {
        'from': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True,
            'empty': False,
        },
        'to': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True,
            'empty': False,
        },
        'content': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1024,
            'required': True,
        },
        'incoming': {
            'type': 'boolean',
            'required': True,
        },
        'hash': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'sms_date': {
            'type': 'datetime',
            'required': True,
            'empty': False,
        }
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'sms': SMS
}
