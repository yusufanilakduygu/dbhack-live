
from pyparsing import *

def parse_ping(pcmd):
    servername=Word(nums+alphas+".")
    portrange=Word(nums)+"-"+Word(nums)
    port=Word(nums)
    ipField = Word(nums, max=3)
    iprange = Combine( ipField + "." + ipField + "." + ipField + "." + ipField + "-" + ipField)

    server_parser="-server"+Group(Or([iprange, delimitedList(servername)])).setResultsName('server')

    port_parser="-port"+  Group(Or([ portrange ,delimitedList(port,",") ])).setResultsName('port')+";"

    Oracle_tnsping_parser=server_parser+port_parser
    result= Oracle_tnsping_parser.parseString(pcmd)
    return result


def oracle_ping(args):
    print (args)
    parsed_command=parse_ping(args)
    print(parsed_command)
    return

def oracle_version(args):
    parsed_command=parse_ping(args)
    print(parsed_command)
    return
