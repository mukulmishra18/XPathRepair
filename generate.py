from utils import chainFunctions
from xpath import XPath

class GenerateXPaths():
     
    def __init__(self, response, field, filename):
        self.response = response
        self.file = open(filename, 'w')
        self.original = response.xpath(field.xpath.xpath).extract()
        XPathList = [field.xpath]
        generators = [self.reducePath]
        XPathList = chainFunctions(generators, XPathList)
        self.writeList(self.file, XPathList)

    def reducePath(self, XPathList):
        newXPaths = []
        for xpath in XPathList:
            newXPaths += self._reducePath(xpath.split())
        for xpath in newXPaths:
            xpath.xpath = "/" + xpath.xpath
        newXPaths = filter(self.validate, newXPaths)
        return XPathList + newXPaths

    def _reducePath(self, parts):
        if len(parts) is 1:
            return []
        if len(parts) is 2:
            return [XPath(parts[1:])]
        return [XPath(parts[1:])] + self._reducePath(parts[1:])

    def validate(self, xpath):
        new = self.response.xpath(xpath.xpath).extract()
        if new == self.original:
            return True
        return False

    def writeList(self, file, XPathList):
        for xpath in XPathList:
            file.write(xpath.xpath + '\n')
    

