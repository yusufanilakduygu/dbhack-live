from dbhack_parser import *
import socket
import itertools
 

def return_string_between(p_data,p_begin,p_end):
	return p_data[p_data.index(p_begin)+len(p_begin) : p_data.find(p_end, p_data.index(p_begin)+len(p_begin)  )]




def mssql_ping(p_server):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(13)

    server_address = (p_server, 1434)
    message =  bytearray ([0x03])
    print(" ")
    print (' Connection : '+p_server)
    try:
        sent = sock.sendto(message, server_address)
        data, server = sock.recvfrom(4096)
    except Exception as error:
        print("")
        print('  Not Connected to SQL Server ' + str(error) )
        print("")
        return
     

    str_data=str(data)
    print() 
    print( "    Server Name   :", return_string_between(str_data,"ServerName;",";"))
    print( "    Instance Name :", return_string_between(str_data,"InstanceName;",";"))
    print( "    Version       :", return_string_between(str_data,"Version;",";"))
    print( "    Port Number   :", return_string_between(str_data,"tcp;",";"))
    print()
    return


def mssql_chk(args):
    parsed_command=parse_mssql_ping(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0]):
                mssql_ping(i[0])
    return
