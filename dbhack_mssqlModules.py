from dbhack_parser import *
import socket
import itertools
import pyodbc

def return_string_between(p_data,p_begin,p_end):
	return p_data[p_data.index(p_begin)+len(p_begin) : p_data.find(p_end, p_data.index(p_begin)+len(p_begin)  )]




def mssql_ping(p_server):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(4)

    server_address = (p_server, 1434)
    message =  bytearray ([0x03])
    print(" ")
    print (' Connection : '+p_server)
    try:
        sent = sock.sendto(message, server_address)
        data, server = sock.recvfrom(4096)
    except Exception as error:
        print("")
        print('  Server or SQL Server Browser did not respond your request ' + str(error) )
        print("")
        sock.close()
        return
     

    str_data=str(data)
    print() 
    print( "    SQL Server Browser responded your request ")
    print()
    print( "    Server Name   :", return_string_between(str_data,"ServerName;",";"))
    print( "    Instance Name :", return_string_between(str_data,"InstanceName;",";"))
    print( "    Version       :", return_string_between(str_data,"Version;",";"))
    print( "    Port Number   :", return_string_between(str_data,"tcp;",";"))
    print( "    Full Returned Data ")
    print() 
    print( "    "+str_data)
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

def mssql_connect (args):
    parsed_command=parse_user_for_mssql(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0], parsed_command[1],parsed_command[2],parsed_command[3],parsed_command[4] ):
                mssql_connect_check(i[0],i[1],i[2],i[3],i[4])
    return

def mssql_chk_odbc (args):
    parsed_command=parse_mssql_check_odbc(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0], parsed_command[1]):
                # mssql_connect_check(i[0],i[1],'MASTER','fakexyz123','fakexyz123')
                print('')
                print (' Connection : '+i[0]+' : '+str(i[1])+'...')
                connect_string='DRIVER={SQL Server};SERVER='+i[0]+','+str(i[1])+';DATABASE=MASTER;UID=fakexyz123;PWD=fakexyz123'
                try:
                      cnxn = pyodbc.connect(connect_string , timeout=1 )
                except Exception as error:
                       # print(str(error), ' find -->  ',str(error).find('Login failed for user'))
                        if str(error).find('Login failed for user') > 0:
                                print("")
                                print (' Connection test is succesfull , There is an SQL Server database in this server and port ')
                                print("")
                                return
                        else:                                  
                                print("")
                                print (' Connection test is NOT succesfull , There is NOT any SQL Server database in this server and port ')
                                print("")
                                return
                print(' GOTCHA Connection is Successfull there is an user with name fakexyz123 and the same password ' )
                return
                cnxn.close        
    return

def mssql_connect_check(p_server,p_port,p_dbname,p_user,p_passwd):

        connect_string='DRIVER={SQL Server};SERVER='+p_server+','+str(p_port)+';DATABASE='+p_dbname+';UID='+p_user+';PWD='+p_passwd
        print(" ")
        print (' Connection Test: '+p_server+';'+str(p_port)+';'+p_dbname+';'+p_user+';'+p_passwd)
        try:
                cnxn = pyodbc.connect(connect_string , timeout=1 )
        except Exception as error:
                print("")
                print('  Not Connected to MSSQL Server ' + str(error) )
                print("")
                return

        print(' Connection is Successfull  ' )
        return
        cnxn.close


def mssql_connect_null_passwd (args):
    parsed_command=parse_user_for_mssql_null_passwd(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0],parsed_command[1],parsed_command[2] ):
                mssql_connect_check(i[0],i[1],'MASTER',i[2],'')

    return

def mssql_brute_with_file (args):
    parsed_command=parse_brute_file_mssql(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in   range(0,len(parsed_command[3])):
                mssql_connect_check(parsed_command[0][0],parsed_command[1][0],parsed_command[2][0] ,parsed_command[3][i][0] , parsed_command[3][i][1] )
    return
        
