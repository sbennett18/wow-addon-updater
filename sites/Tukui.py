###
# Tukui
class TukuiSite(SiteSplitter):
    NETLOCS = ("git.tukui.org",)

    def __init__(self, addonpageParts):
        super().__init__(addonpageParts)
        self.username, self.repository = self.name.split("/")

    @property
    def downloadLink(self):
        try:
            return self._downloadLink
        except AttributeError:
            pass

        branch = "master"
        archive = f"{self.repository}-{branch}.zip"
        self._downloadLink = "/".join((self.url, "-", "archive", branch, archive))
        return self._downloadLink

    @property
    def version(self):
        try:
            return self._version
        except AttributeError:
            pass

        try:
            response = requests.get(self.url)
            response.raise_for_status()
            content = str(response.content)
            match = re.search(
                r'<div class="commit-sha-group">\\n<div class="label label-monospace">\\n(?P<hash>[^<]+?)\\n</div>',
                content,
            )
            self._version = match.group("hash").strip() if match else ""
        except Exception as err:
            self._version = ""
            print("Failed to find version number for:", self.url)
            print(err)

        return self._version