from pyparsing import *
from dbhack_error_module import error_module

"""
25.07.2017
This function parses ping commands
It has two parts : One part is the server parameters with -server option
other part is the port part with -port option
Server part can contain  ; server names , ip names with comma ;  -server 192.178.10.4, db.local.org
or this part can contains a network segment like : 192.168.10.1-45
There is no more selection for this option
Port part can contain; port numbers or one port range like;
1521,1522,1527   or  1500-1600
There is no more selection for this option
return_list is the output of this function;  This list contains two lists
return_list[0] --> Server list
return_list[1] --> port list in number format
Sample Calls:
ping -s ip,servername -p port1,port2
ping -s xxx.xxx.xxx.xx-xx -p port1-port2
print(parse_ping("-s kw1-1.com  -p  125 ; "))
print(parse_ping("-s kw1-1.com  -p  125 -127; "))
print(parse_ping("-s 192.200.11.9-10  -p  125 -126; "))
print(parse_ping("-s 192.200.11.9   -p  125 ; "))
print(parse_ping("-s 192.200.11.9-10   -p  125 , 126; "))
print(parse_ping("-s   a2  -p  125  ; "))
print(parse_ping("-s 192.200.11.9, 192.200.11.9 ,a3, 192.200.11.12  -p  125 , 126; "))
print(parse_ping("-s 192.200.11.9-10,192.200.11.9   -p  125 -126; ")) Gives error
print(parse_ping("-s kw1-1.com, kw2-1.com  -p  125 -127; "))
print(parse_ping("-s kw1-1.com, kw2-1.com , 192.200.11.9, 192.200.11.11 -p  125 -127; "))
"""

def parse_ping(pcmd):

    ipField = Word(nums, max=3)

    full_ip     =  Combine(ipField + "." + ipField + "." + ipField + "." + ipField )
    
    servername=(Combine(Word(alphas,min=1)+Word(alphas+nums+"."+"-")))

    servernames= Or([full_ip , servername])
    
    portrange=Word(nums)+"-"+Word(nums)
    
    port=Word(nums)
    

    iprange     =  ipField + "." + ipField + "." + ipField + "." + ipField + "-" + ipField
    
    
    server_parser="-s"+Group(Or([  iprange , delimitedList(servernames)])).setResultsName('server')

    port_parser="-p"+  Group(Or([ portrange ,delimitedList(port,",") ])).setResultsName('port')

    Oracle_tnsping_parser= (server_parser & port_parser )+";"
    
    return_list=list()
    
    try:
        parse_result= Oracle_tnsping_parser.parseString(pcmd)
    except ParseException:
        error_module('parse_ping_010','ParseException from dbhack_parser.parse_ping','Your command can not be parsed')
        return_list=['Error']
        return return_list
        

   
    
    server_list =list(parse_result['server'])
    port_list   =list(parse_result['port'])


    server_range_list=list()
    
    # Server is ip range
    if '-' in server_list :
        
        # Check ip range list
        
        if int(server_list[6])  >=  int(server_list[8]):
            error_module('parse_ping_030','IP range condition check at dbhack_parser.parse_ping','IP Range is not correct')
            return_list=['Error']
            return return_list
        
        #Check IP less than 255

        
        if int(server_list[6]) > 255 or int(server_list[8]) > 255 or int(server_list[0]) > 255 or int(server_list[2]) > 255 or int(server_list[4]) > 255:
            error_module('parse_ping_040','IP range condition check at dbhack_parser.parse_ping','IPs greater than 255')
            return_list=['Error']
            return return_list 
        
        # Prepare IPs
        
        domain_ip = server_list[0]+'.'+server_list[2]+'.'+server_list[4]+'.'
        
        for x in range(int(server_list[6]),int(server_list[8])+1):
            server_range_list.append(domain_ip+str(x))
            
        return_list.append(server_range_list)
                
    else:
       # if there is no ip range put server_list into return list directly
        return_list.append(server_list)
        
    # port is in ip range

    portrange_list=list()
    
    if '-' in port_list:
        
    # if there is port range , produce port range list
    
        if int(port_list[0])  >=  int(port_list[2]):
            error_module('parse_ping_020','Port range condition check at dbhack_parser.parse_ping','Port Range is not correct')
            return_list=['Error']
            return return_list
        
        if int(port_list[0])  > 65535 or   int(port_list[2]) > 65535 :
            error_module('parse_ping_050','Port range condition check at dbhack_parser.parse_ping','Port is greater than 65535')
            return_list=['Error']
            return return_list
        
        # Prepare port range list
        for x in range(int(port_list[0]),int(port_list[2])+1):
            portrange_list.append(x)

        return_list.append(portrange_list)
    else:
          if len([ x for x in port_list if int(x) > 65535]):
            error_module('parse_ping_060','Port range condition check at dbhack_parser.parse_ping','Port numbers can not be greater than 65535')
            return_list=['Error']
            return return_list
        
          for i in range(len(port_list)):
              portrange_list.append(int(port_list[i]))

          return_list.append(portrange_list)
          
    return return_list
