class Field():

    def __init__(self, field, xpath):
        if isinstance(xpath, basestring):
            xpath = XPath(xpath)
        self.xpath = xpath
        self.field = field

class XPath():

    def __init__(self, xpath):
        if type(xpath) is list:
            self._join(xpath)
        else:
            self.xpath = xpath
    
    def _join(self, parts):
        if str(parts[0]) == "//":
            self.xpath = "//" + "/".join(map(str, parts[1:]))
        else:
            self.xpath = "/" + "/".join(map(str, parts))

    def split(self):
        parts = self.xpath.split('/')
        del parts[0]
        if not parts[0]:
            parts[0] = '//'
        return map(Component, parts)

    def __str__(self):
        return self.xpath

    def __repr__(self):
        return self.xpath

class Component():

    def __init__(self, component):
        self.component = component

    def __str__(self):
        return self.component

    def __repr__(self):
        return self.component

