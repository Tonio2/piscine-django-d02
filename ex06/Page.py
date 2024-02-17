from elem import Elem, Text
from elements import *

class Page:
    def __init__(self, elem):
        if not issubclass(type(elem), Elem):
            raise TypeError("The element must be an instance of Elem or its subclasses.")
        self.root = elem

    def is_valid(self):
        return self.__is_valid_node(self.root, None)

    def __is_valid_node(self, node, parent):
        # Define rules based on node type and parent type
        valid_elements = {
            'html': ['head', 'body'],
            'head': ['title'],
            'body': ['h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'text'],
            'div': ['h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'text'],
            'title': ['text'],
            'h1': ['text'],
            'h2': ['text'],
            'li': ['text'],
            'th': ['text'],
            'td': ['text'],
            'p': ['text'],
            'span': ['text', 'p'],
            'ul': ['li'],
            'ol': ['li'],
            'tr': ['th', 'td'],
            'table': ['tr'],
        }

        if parent and node.tag not in valid_elements.get(parent.tag, []):
            return False

        if node.tag == 'html':
            head_count = sum(1 for c in node.content if isinstance(c, Head))
            body_count = sum(1 for c in node.content if isinstance(c, Body))
            if head_count != 1 or body_count != 1:
                return False

        if node.tag == 'head':
            title_count = sum(1 for c in node.content if isinstance(c, Title))
            if title_count != 1:
                return False
        
        if node.tag in ['h1', 'h2', 'li', 'th', 'td', 'title']:
            text_count = sum(1 for c in node.content if isinstance(c, Text))
            if text_count != 1:
                return False
            
        if node.tag in ['ul', 'ol']:
            li_count = sum(1 for c in node.content if isinstance(c, Li))
            if li_count == 0:
                return False
            
        if node.tag == 'tr':
            th_count = sum(1 for c in node.content if isinstance(c, Th))
            td_count = sum(1 for c in node.content if isinstance(c, Td))
            if th_count == 0 and td_count == 0:
                return False
            if th_count > 0 and td_count > 0:
                return False
        
        if node.tag == 'table':
            tr_count = sum(1 for c in node.content if isinstance(c, Tr))
            if tr_count == 0:
                return False

        for child in node.content:
            if not isinstance(child, (Elem, Text)):
                return False
            if isinstance(child, Elem) and not self.__is_valid_node(child, node):
                return False

        return True

    def __str__(self):
        doctype = "<!DOCTYPE html>\n" if isinstance(self.root, Html) else ""
        return doctype + str(self.root)

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

if __name__ == '__main__':
    html = Html([Head(Title(Text("My Page"))), Body()])
    page = Page(html)
    print(page.is_valid())  # Should return True if the page structure is valid
    print(page)  # Print the HTML representation
    page.write_to_file("output.html")  # Write to a file
    
    # Test invalid page
    print("\nTest invalid page with double body:")
    html = Html([Head(Title(Text("My Page"))), Body(H1(Text("Hello World"))), Body()])
    page = Page(html)
    print(page.is_valid())  # Should return False if the page structure is invalid
    
    html = Html([Head(Title(Text("My Page"))), Body(H1(Text("Hello World")))])
    page = Page(html)
    print(page.is_valid()) 
    
    # Test multiple text elements in title
    print("\nTest invalid page with multiple text elements in title:")
    html = Html([Head(Title([Text("My Page"), Text("My Page")])), Body()])
    page = Page(html)
    print(page.is_valid())  # Should return False if the page structure is invalid
    
    html = Html([Head(Title([Text("My Page")])), Body()])
    page = Page(html)
    print(page.is_valid())  
    
    # Test th and td in same tr
    print("\nTest invalid page with th and td in same tr:")
    html = Html([Head(Title(Text("My Page"))), Body(Table(Tr([Th(Text("Header")), Td(Text("Data"))])))])
    page = Page(html)
    print(page.is_valid())  # Should return False if the page structure is invalid
    
    html = Html([Head(Title(Text("My Page"))), Body(Table(Tr([Td(Text("Header")), Td(Text("Data"))])))])
    page = Page(html)
    print(page.is_valid()) 
