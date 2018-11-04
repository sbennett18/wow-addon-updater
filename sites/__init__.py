from urllib.parse import urlsplit
from pkgutil import iter_modules
from importlib import import_module

for (_, name, _) in iter_modules(("sites",)):
    import_module(f".{name}", __package__)

SITES_MAP = dict()
for site in tuple(SiteSplitter.SiteSplitter.__subclasses__()):
    for nl in site.NETLOCS:
        SITES_MAP[nl] = site


def siteFactory(link):
    parts = urlsplit(link)
    try:
        return SITES_MAP[parts.netloc](parts)
    except KeyError:
        return None
