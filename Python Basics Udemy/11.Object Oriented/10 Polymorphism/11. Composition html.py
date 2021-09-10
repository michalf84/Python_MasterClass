class Tag(object):

    def __init__(self,name,contents):
        self.start_tag='<{}>'.format(name)
        self.end_tag='</{}>'.format(name)
        self.contents=contents

    def __str__(self):
        return"{0.start_tag}{0.contents}{0.end_tag}".format(set)

    def display(self):
        print(self)

class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" http://www.w3.org/TR/REC-html40/strict.dtd','')
        self.end_tag='' #doc type does not have an end tag

class Head(Tag):

    def __init__(self):
        super().__init__('head','')

class Body(Tag):

    def __init__(self):
        super().__init__('body','') # body contentswiil be built up sepearately

    def add_tag(self,name,contents):
        new_tag=Tag(name,contents)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.contents+=str(tag)

        super().display()

class HtmlDoc(object):

    def __initi__(self):
        self._doc_type=DocType()
        self._head=Head()
        self._body=Body()

    def add_tag(self,name,contents):
        self._body.add_tag(name,contents)

    def display(self):
        self._doc_type.display()
        print('<hmtl>')
        self._head.display()
        self._body.display()
        print('</html>')

if __name__=='__main__':
    my_page=HtmlDoc()
    my_page.add_tag('h1','Main heading')
    my_page.add_tag('h2','sub-heading')
    my_page.add_tag('p','This is a parhahgpr on page')
    my_page.display()
