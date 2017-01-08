print " ---------- log ----------"
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print "now ..."

now()

print " ---------- log2 ----------"

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

print "------------ before n after ------------"

def log4(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print 'Before %s %s():' % (text, func.__name__)
            func(*args, **kw)
            print 'After %s %s():' % (text, func.__name__)
            return 
        return wrapper
    return decorator

@log4('run')
def now4():
    print "now4 ..."

now4()

print " ---------- log3 ----------"

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
