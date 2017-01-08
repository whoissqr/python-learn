def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print "now ..."

now()

print "-------------------------"

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('run')
def now2():
    print "now2 ..."

now2()

print "-------------------------"

import functools

def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log3
def now3():
    print "now3 ..."

now3()



print "------------ before n after ------------"

import functools

def log4(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'before call %s():' % func.__name__
        func(*args, **kw)
        print 'after call %s():' % func.__name__
        return 
    return wrapper

@log4
def now4():
    print "now4 ..."

now4()
