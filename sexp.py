import re, os

def load(fname):
    with open(os.path.expanduser(fname)) as fp:
        return parse(fp.read())

def parse(s):
    result, stack = [], []
    idx = 0

    while True:
        c = s[idx:idx+1]

        if c == '(':
            stack.append(result)
            result = []
            idx += 1

        elif c == ')':
            cur, result = result, stack.pop()
            result.append(cur)
            idx += 1
        
        elif re.search('[a-zA-Z:!@#]', c):
            m = re.search('([\w:!@#-]+)', s[idx:])
            value = m.group()
            if value == 'nil':
                result.append([])
            else:
                result.append(value)
            idx += len(m.group())

        elif c == '"':
            m = re.search('("[^"]+")', s[idx:])
            result.append(m.group())
            idx += len(m.group())

        elif re.search('[-\d]', c):
            m = re.search('(-?\d+\.\d+)|(-?\d+)', s[idx:])
            value = float(m.group())
            if value.is_integer():
                value = int(value)
            result.append(value)
            idx += len(m.group())

        else:
            idx += 1

        if idx > len(s):
            break

    if stack:
        raise ValueError('Unbalanced parens: %r' % s)

    (sexp,) = result
    return sexp
