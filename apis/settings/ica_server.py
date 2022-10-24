from .base import *
import os
import dj_database_url
import re

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '^mm-24*°111sdf0(&%%i-6iecm7c@z9lsadflkj84792373sdfl%^ns^4g^z!8=dgffg4ulggr-4=1%'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DEV_VERSION = os.environ.get('APIS_DEV_VERSION', False)

DATABASES = {}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

CSRF_TRUSTED_ORIGINS = ['ica.acdh.oeaw.ac.at']

APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']


# SECURITY WARNING: don't run with debug turned on in production!

APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False
REDMINE_ID = "17197"

#REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
#    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
#)

ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,ica.acdh-dev.oeaw.ac.at,.acdh-cluster.arz.oeaw.ac.at"),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

PROJECT_NAME = "ica"
APIS_BASE_URI = "https://ica.acdh-dev.oeaw.ac.at"
APIS_BLAZEGRAPH = (
    'https://blazegraph.herkules.arz.oeaw.ac.at/omnipot/sparql',
    os.environ.get('APIS_BLAZEGRAPH_USER'),
    os.environ.get('APIS_BLAZEGRAPH_PASSWORD')
)


LANGUAGE_CODE = "de"

TRANSKRIBUS = {
    "user": os.environ.get('APIS_TRANSKRIBUS_USER'),
    "pw": os.environ.get('APIS_TRANSKRIBUS_PASSWORD'),
    "col_id": "50328",
    "base_url": "https://transkribus.eu/TrpServer/rest"
}

APIS_SKOSMOS = {
    'url': os.environ.get('APIS_SKOSMOS', 'https://vocabs.acdh-dev.oeaw.ac.at'),
    'vocabs-name': os.environ.get('APIS_SKOSMOS_THESAURUS', 'icathesaurus'),
    'description': 'Thesaurus of the ICA project. Used to type entities and relations.'
}

REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = (
        #"rest_framework.permissions.DjangoModelPermissions"
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        #"rest_framework.permissions.DjangoObjectPermissions",
        # use IsAuthenticated for every logged in user to have global edit rights
    )


####### ROBOTS.TXT HANDLING #######

# robots.txt file needs to be located in a folder that is registered as a template-dir
# both the end of the url from where the file is served as well as the file itself needs to be named robots.txt
# if you want to add your own robots txt, create a new folder in the root directory and register it here

# replace the path to the folder in which the robots.txt file is to be found here
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")

# register above folder as a template-dir
TEMPLATES[0]["DIRS"] += [ROBOTS_TXT_FOLDER,]

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://174a0f192d064beaab3513f30e922576@sentry.acdh-dev.oeaw.ac.at/14",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
