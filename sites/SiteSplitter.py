###
# SiteSplitter Base Class
class SiteSplitter:
    def __init__(self, addonpageParts):
        self.url = addonpageParts.geturl()
        self.netloc = addonpageParts.netloc
        # Expected input format: "mydomain.com/myzip.zip" or "mydomain.com/myzip.zip|subfolder"
        self.path, *self.subfolders = addonpageParts.path.split("|")
        self.path = self.path.strip("/")  # Remove leading/trailing '/'s
        if self.path.endswith("/files"):
            self.name = self.path.rsplit("/", 1)[0]
        else:
            self.name = self.path
