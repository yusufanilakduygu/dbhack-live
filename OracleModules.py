
from dbhackparser import *

def oracle_ping(args):
    print (args)
    parsed_command=parse_ping(args+" ;")
    print(parsed_command)
    return

def oracle_version(args):
    parsed_command=parse_ping(args+" ;")
    print(parsed_command)
    return
