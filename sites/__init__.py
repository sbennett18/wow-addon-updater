from urllib.parse import urlsplit
from importlib import import_module
from .SiteSplitter import SiteSplitter

SITES = tuple(SiteSplitter.__subclasses__())
SITES_CLASS_MAP = dict()
for site in SITES:
    for nl in site.NETLOCS:
        SITES_CLASS_MAP[nl] = site


def siteFactory(link):
    parts = urlsplit(link)
    try:
        return SITES_CLASS_MAP[parts.netloc](parts)
    except KeyError:
        return None
