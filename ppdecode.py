import urlparse, re
import sys

class ppdecode(object):
    def __init__(self, url):
        self.pplink = url
        self.arguments = urlparse.parse_qs(urlparse.urlparse(url).query)
        self.url = self._decodeurl()
        self._parse()

    def _decodeurl(self):
        tmp = self.arguments['u'][0].replace("_","/")
        for x in list(set(re.findall('-[0-9A-F]{2,2}', tmp))):
            tmp = tmp.replace(x,chr(int(x[1:3],16)))
        return tmp

    def _parse(self):
        if "r" in self.arguments:
            self.recipient = self.arguments['r'][0]
        if "c" in self.arguments:
            self.site = self.arguments['c'][0]
        pass

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        sys.exit('Usage: ppdecode.py "http://url"')
    url = sys.argv[1]
    p = ppdecode(url)
    print p.url
