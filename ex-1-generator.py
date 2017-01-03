def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
        
print '------------- [generator] ------------'
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

print '------------- [generator] ------------'       
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        
for n in fib2(6):
    print n

print '------------- [higher order function] ------------'
def add(x, y, f):
    return f(x) + f(y)

print '-------------  [function as argument] ------------'
print add(-8,9, abs)

print '------------- [map/reduce]------------'

def fn(x, y):
     return x * 10 + y

def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print map(char2num, '13579')

k = reduce(fn, map(char2num, '13579'))

print k

print '------------- [map/reduce]------------'

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print str2int('11130')
