from elem import Elem, Text

class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='html', attr=attr, content=content)
  
class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='head', attr=attr, content=content)
  
class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='body', attr=attr, content=content)
  
class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='title', attr=attr, content=content)
  
class Meta(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')
  
class Img(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='img', attr=attr, content=content, tag_type='simple')

class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='table', attr=attr, content=content)
  
class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='th', attr=attr, content=content)
  
class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='tr', attr=attr, content=content)
  
class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='td', attr=attr, content=content)
  
class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='ul', attr=attr, content=content)
  
class Ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='ol', attr=attr, content=content)
  
class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='li', attr=attr, content=content)
  
class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='h1', attr=attr, content=content)
  
class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='h2', attr=attr, content=content)
  
class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='p', attr=attr, content=content)
  
class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='div', attr=attr, content=content)
  
class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='span', attr=attr, content=content)
  
class Hr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='hr', attr=attr, content=content, tag_type='simple')

class Br(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='br', attr=attr, content=content, tag_type='simple')
  
if __name__ == '__main__':
	print("Testing Html class...")
	assert str(Html()) == '<html></html>'
	assert str(Html(Text('foo'))) == '<html>\n  foo\n</html>'
	assert str(Html(Text('foo'))) == '<html>\n  foo\n</html>'
	assert str(Html([Html(Text('foo'))])) == '<html>\n  <html>\n    foo\n  </html>\n</html>'
	assert str(Html([Html(Text('foo')), Html(Text('bar'))])) == '<html>\n  <html>\n    foo\n  </html>\n  <html>\n    bar\n  </html>\n</html>'
	print("Html class OK.")
	print("Testing Head class...")
	assert str(Head()) == '<head></head>'
	assert str(Head(Text('foo'))) == '<head>\n  foo\n</head>'
	assert str(Head(Text('foo'))) == '<head>\n  foo\n</head>'
	assert str(Head([Head(Text('foo'))])) == '<head>\n  <head>\n    foo\n  </head>\n</head>'
	assert str(Head([Head(Text('foo')), Head(Text('bar'))])) == '<head>\n  <head>\n    foo\n  </head>\n  <head>\n    bar\n  </head>\n</head>'
	print("Head class OK.")
	print("Ful HTML page test with all elements...")
	print(str(Html([Head([Title(Text("Hello ground!")), Meta(attr={'charset': 'utf-8'})]), Body([H1(Text("Oh no, not again!")), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])])))
 
 