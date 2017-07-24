from pyparsing import *

"""

General ping parser

ping -server,ip,servername -port port1,port2
ping -server xxx.xxx.xxx.xx-xx -port port1-port2
-server 192.178.45.12, 123.56.56.78  -port 123,678  ; 

print(parse_ping("-server x, y   -port 123-67; "))
print(parse_ping("-server x, y   -port 123,67; "))
print(parse_ping("-server 172.345.456.12-256   -port 123-67; "))
print(parse_ping("-server 172.345.456.12-256   -port 123,67; "))
print(parse_ping("-server 172.345.456.12-256   -port 67-123; "))

print(parse_ping("-server 172.345.456.256   -port 125-123; "))

return result['server']
return result['port']
"""

def parse_ping(pcmd):
    servername=Word(nums+alphas+".")
    portrange=Word(nums)+"-"+Word(nums)
    port=Word(nums)
    ipField = Word(nums, max=3)
    iprange =  ipField + "." + ipField + "." + ipField + "." + ipField + "-" + ipField

    server_parser="-server"+Group(Or([iprange, delimitedList(servername)])).setResultsName('server')

    port_parser="-port"+  Group(Or([ portrange ,delimitedList(port,",") ])).setResultsName('port')+";"

    Oracle_tnsping_parser=server_parser+port_parser
    try:
        result= Oracle_tnsping_parser.parseString(pcmd)
    except ParseException:
        print('')
        print ('Error No    : Error-02 ')
        print ('Module      : ParseException from dbhack_parser.parse_ping ')
        print ('Explanation : Your command can not be parsed please type')
        print ('              help command_name to see command samples')
        print('')
        result=['Error-01']
        
    print(result['server'])

    # Server is ip range
    
    if '-' in list(result['server']):
        print( 'in server list')
        
    # port is in ip range   
    if '-' in list(result['port']):
        portrange_list=list()
        port_start=int(list(result['port'][0]))
        port_end  =int(list(result['port'][2]))
        print(port_start,port_end,'******')
        if port_start >= port_end :
                print('')
                print ('Error No    : Error-02 ')
                print ('Module      : ParseException from dbhack_parser.parse_ping ')
                print ('Explanation : Port Range is not correct')
                print('')
                result=['Error-01']    

    print(result['port'])
    return result












