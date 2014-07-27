import sexp
import pytest

testcases = [
    ('()', []),
    ('(a)', ['a']),
    ('(a b c)', ['a', 'b', 'c']),
    ('(1 1.1 -1 -1.1)', [1, 1.1, -1, -1.1]),
    ('(1 2 a b c)', [1, 2, 'a', 'b', 'c']),
    ('(a (b c) d (1 2 3))', ['a', ['b', 'c'], 'd', [1, 2, 3]]),
    ('(1 nil 3)', [1, [], 3]),
    ('(1 "foo" b)', [1, '"foo"', 'b']),
    ('(:name "eric" :age 25)', [':name', '"eric"', ':age', 25]),

    # http://rosettacode.org/wiki/S-Expressions
    ('''((data "quoted data" 123 4.5)
      (data (!@# (4.5) "(more" "data)")))''',

     [['data', '"quoted data"', 123, 4.5],
      ['data', ['!@#', [4.5], '"(more"', '"data)"']]]),
]

def test_sexp_exception():
    for sexp_input, parsed in testcases:
        assert sexp.parse(sexp_input) == parsed

    with pytest.raises(ValueError):
        sexp.parse('(1 (2 3)')
