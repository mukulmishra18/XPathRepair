from os.path import isfile
from field import XPath, Field
from generate import GenerateXPaths

class XPathRepair():

    def __init__(self, response):
        self.response = response
        self.XPathFilename = 'xpaths.txt'

    def process(self, field, xpath):
        field = Field(field, xpath)
        self.Generate(field)
        if self.IsAnomaly(field.xpath):
            field = self.Repair(field)
        return self.Extract(field)

    def Generate(self, field):
        if isfile(self.XPathFilename):
            return
        GenerateXPaths(self.response, field, self.XPathFilename)
        
    def Extract(self, field):
        return self.response.xpath(field.xpath.xpath).extract()

    def Repair(self, field):
        with open(self.XPathFilename, 'r') as f:
            for line in f:
                if not self.IsAnomaly(XPath(line)):
                    return Field(field.field, XPath(line))
            return field
                    
    
    def IsAnomaly(self, xpath):
        if self.response.xpath(xpath.xpath).extract() == []:
            return True
        return False
