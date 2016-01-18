from os.path import isfile
from field import XPath, Field
from generate import GenerateXPaths

class XPathRepair():

    def __init__(self, response):
        self.response = response
        self.XPathFilename = 'xpaths.txt'

    def process(self, field, xpath):
        field = Field(field, xpath)
        self.generate(field)
        if self.isAnomaly(field.xpath):
            field = self.repair(field)
        return self.extract(field)

    def generate(self, field):
        if isfile(self.XPathFilename):
            return
        GenerateXPaths(self.response, field, self.XPathFilename)
        
    def extract(self, field):
        return self.response.xpath(field.xpath.xpath).extract()

    def repair(self, field):
        with open(self.XPathFilename, 'r') as f:
            for line in f:
                if not self.isAnomaly(XPath(line)):
                    return Field(field.field, XPath(line))
            return field
                    
    def isAnomaly(self, xpath):
        if self.response.xpath(xpath.xpath).extract() == []:
            return True
        return False
