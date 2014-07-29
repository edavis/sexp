sexp.py
=======

`sexp.py` is a python module for parsing [symbolic expressions](http://en.wikipedia.org/wiki/S-expression):

Usage
-----

```python
>>> import sexp
>>> sexp.parse('()')
[]
>>> sexp.parse('(a b c)') # symbols are strings
['a', 'b', 'c']
>>> sexp.parse('(1 1.1 -1 -1.1)') # numbers are parsed as such
[1, 1.1, -1, -1.1]
>>> sexp.parse('(a nil (c d))') # nil is an empty list
['a', [], ['c', 'd']]

>>> # Strings
>>> sexp.parse('("Hello World")') # by default, strings lose their quotes ...
['Hello World']
>>> sexp.parse('("Hello World")', strip_quotes=False) # ... but that's optional
['"Hello World"']

>>> # Advanced
>>> sexp.parse('(:name eric :skills (python django))') # plists
[':name', 'eric', ':skills', ['python', 'django']]
>>> sexp.parse('(#("Hello World" 0 11 (:parent #0)))') # text properties
[['Hello World', 0, 11, [':parent', '#0']]]
>>> sexp.load('~/sexp.txt') # helper function to load from a file
[1, ['a', 'b'], 2]
```

It was designed to handle sexps generated by Emacs, so it
intelligently handles
[text properties](http://www.gnu.org/software/emacs/manual/html_node/elisp/Text-Props-and-Strings.html).

Check out `sexp_test.py` for more examples.

License
-------

BSD
