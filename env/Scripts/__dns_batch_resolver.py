#!C:\Users\Sirius\Documents\rimgro\sat07.03\sat\env\Scripts\python.exe

from sys import argv, stderr
from dns_batch_resolver import cleanup, resolv, query

if argv[1] == '--cleanup':
    print >> stderr, ('cleanup')
    cleanup()
elif argv[1] == '--resolv':
    print >> stderr, ('resolv')
    resolv()
elif argv[1] == '--query':
    print >> stderr, ('query')
    query()
else:
    raise ValueError(argv, message='Unknown args')
