from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "172.20.0.3",
    "172.20.0.1",
    "apis-oebl.sisyphos.arz.oeaw.ac.at",
    "apis.acdh.oeaw.ac.at",
    "*",
]

INSTALLED_APPS += [
    'csp',
    # other apps
]


CSP_DEFAULT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "data: 'unsafe-eval'",
    "cdnjs.cloudflare.com",
    "cdn.jsdelivr.net",
    "fonts.googleapis.com",
    "ajax.googleapis.com",
    "cdn.rawgit.com",
    "*.acdh.oeaw.ac.at",
    "unpkg.com",
    "fonts.gstatic.com",
    "cdn.datatables.net",
    "code.highcharts.com",
    "*.acdh-dev.oeaw.ac.at",
    "*.acdh.oeaw.ac.at",
    "openstreetmap.org",
    "*.openstreetmap.org",
    "*.placeholder.com",
)

CSP_SCRIPT_SRC = CSP_DEFAULT_SRC + (
    "https://unpkg.com",
    "'unsafe-eval'",
)


DEV_VERSION = os.environ.get("APIS_DEV_VERSION", True)

BIRTH_REL_ID = 595
DEATH_REL_ID = 596


INSTALLED_APPS += [
    "apis_highlighter",
    "haystack",
    "theme",
    "leaflet",
    "sass_processor",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("APIS_DB_NAME"),
        "USER": os.environ.get("APIS_DB_USER"),
        "PASSWORD": os.environ.get("APIS_DB_PASSWORD"),
        "HOST": os.environ.get("APIS_DB_HOST", "127.0.0.1"),
        "PORT": os.environ.get("APIS_DB_PORT", "3306"),
    }
}

X_FRAME_OPTIONS = "ALLOW-FROM http://sennierer.github.io/"

APIS_LOCATED_IN_ATTR = ["located in", "situated in"]

APIS_SEARCH_CAREER = [
    "war Militär",
    "war Mitarbeiter von",
    "war Aufsichtsratsmitglied",
    "war Miteigentümer von",
    "war Politiker",
    "war Mitglied",
]

APIS_SEARCH_EDUCATION = ["war in Ausbildung"]

APIS_SEARCH_TEXTTYPES = ["ÖBL Haupttext", "ÖBL Kurzinfo"]

APIS_SEARCH_ANNOTATION_PROJECTS = [
    "Rumpolt Diss Nachrecherche",
    "Rumpolt Diss",
    "trainings data 300 select names",
    "Gold Standard 11.06.2018",
    "Gold Standard 22.05.2018",
    "Rumpolt Evaluation",
    "Andrássy",
    "Pressenetzwerke Ágoston",
    "Hungarian Journalists 12-2017",
    "Gold Standard 28.3.2017",
    "300 select names",
    "Mittelalter",
    "Künstlerhaus Maximilian",
    "Klausenburg Agoston",
    "Default",
]

APIS_SEARCH_EXCLUDE_NAMES = ["(Dummy)"]

APIS_SHOW_ONLY_PUBLISHED = True

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.solr_backend.SolrEngine",
        "URL": "http://apis-solr:8983/solr/apis_solr",
        "ADMIN_URL": "http://apis-solr:8983/solr/admin/cores",
    }
}

APIS_API_EXCLUDE_SETS = True

FEATURED_COLLECTION_NAME = "FEATURED"
MAIN_TEXT_NAME = "ÖBL Haupttext"
BIRTH_REL_NAME = "geboren in"
DEATH_REL_NAME = "gestorben in"
APIS_BASE_URI = "https://apis.acdh.oeaw.ac.at/"
APIS_OEBL_BIO_COLLECTION = "ÖBL Biographie"


REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = (
    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
)

CSRF_TRUSTED_ORIGINS = ["https://apis.acdh.oeaw.ac.at"]

APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]

REDMINE_ID = "17784"

APIS_BASE_URI = "https://apis.acdh.oeaw.ac.at/"

APIS_SKOSMOS = {
    "url": os.environ.get("APIS_SKOSMOS", "https://vocabs.acdh-dev.oeaw.ac.at"),
    "vocabs-name": os.environ.get("APIS_SKOSMOS_THESAURUS", "apisthesaurus"),
    "description": "Thesaurus of the APIS project. Used to type entities and relations.",
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://52a791b36a6f459e8c8b801677ec304c@sentry.io/1882721",
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)

SASS_ROOT = os.path.join(BASE_DIR, "theme", "static", "theme", "scss", "fundament_oebl")

SASS_PROCESSOR_ROOT = SASS_ROOT

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

PROJECT_NAME = "apis"
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")
