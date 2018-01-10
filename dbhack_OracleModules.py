from dbhack_parser import *
import socket
import itertools
import cx_Oracle


def tns_ping(p_servername,p_port):
    sock= socket.socket()
    sock.settimeout(5)
    try:
        print('')
        print (' Connection : '+p_servername+' : '+str(p_port)+'...')
        sock.connect((p_servername, p_port))
    except Exception as error:
        print("")
        print('  Not Connected to Server ' + str(error))
        print("")
        sock.close()
        return
    print('  Connected to the port')	

    # Message sent: (CONNECT_DATA=(COMMAND=ping)) ODB
    # to check listener is running
    
    send_msg= bytearray ([0x00, 0x57, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 
    0x01, 0x3a, 0x01, 0x2c, 0x00, 0x00, 0x20, 0x00, 
    0x7f, 0xff, 0xc6, 0x0e, 0x00, 0x00, 0x01, 0x00, 
    0x00, 0x1d, 0x00, 0x3a, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x28, 0x43, 0x4f, 0x4e, 0x4e, 0x45, 
    0x43, 0x54, 0x5f, 0x44, 0x41, 0x54, 0x41, 0x3d, 
    0x28, 0x43, 0x4f, 0x4d, 0x4d, 0x41, 0x4e, 0x44, 
    0x3d, 0x70, 0x69, 0x6e, 0x67, 0x29, 0x29 ] )
    try:	
    	sock.send(send_msg)
    	msg = sock.recv(2048)
    except Exception as error:
        print("")
        print('  After port connection Error ' + str(error))
        print("")
        sock.close()
        return
    decoded_msg=msg.decode('ascii')
    i=decoded_msg.find('ERR=0')
    if i != -1:
        print ('  Oracle Listener Found')  
        print('    Listener Name : ',msg.decode('ascii')[msg.decode('ascii').find("ALIAS=")+6:-2], end="")
        print()
    else:
        print ("  Oracle Listener Not Found")
        print()
        sock.close()
        return

  # message to send (CONNECT_DATA=(COMMAND=version))

    send_msg= bytearray ([
    0x00, 0x5a, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 
    0x01, 0x36, 0x01, 0x2c, 0x00, 0x00, 0x08, 0x00, 
    0x7f, 0xff, 0x7f, 0x08, 0x00, 0x00, 0x00, 0x01, 
    0x00, 0x20, 0x00, 0x3a, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x34, 0xe6, 0x00, 0x00, 
    0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x28, 0x43, 0x4f, 0x4e, 0x4e, 0x45, 
    0x43, 0x54, 0x5f, 0x44, 0x41, 0x54, 0x41, 0x3d, 
    0x28, 0x43, 0x4f, 0x4d, 0x4d, 0x41, 0x4e, 0x44, 
    0x3d, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 
    0x29, 0x29 ])


    sock.close()
    sock= socket.socket()
    sock.connect((p_servername, p_port))
    
    sock.send(send_msg)
    msg = sock.recv(2048)
    ascii_message=str(msg)
    vssnum_loc=ascii_message.find('VSNNUM=')
    version_number=hex(int(ascii_message[vssnum_loc+7:vssnum_loc+7+9]))
    sock.close()
    print('    DB version    : ' ,
       str(int(version_number[2:3],16))+'.'+
       str(int(version_number[3:4],16))+'.'+
       str(int(version_number[4:6],16))+'.'+
       str(int(version_number[6:7],16))+'.'+
       str(int(version_number[7:9],16))
      )
    print()

        
    return

def ora_chk(args):
    parsed_command=parse_ping(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0], parsed_command[1]):
                tns_ping(i[0],i[1])
    return

def ora_chk_sid(args):
    parsed_command=parse_sid(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0], parsed_command[1],parsed_command[2]):
                oracle_sid_test(i[0],i[1],i[2])
    return

def ora_connect (args):
    parsed_command=parse_user(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0], parsed_command[1],parsed_command[2],parsed_command[3],parsed_command[4] ):
                ora_connect_test(i[0],i[1],i[2],i[3],i[4])
    return


def ora_brute_with_file (args):
    parsed_command=parse_brute_file(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in   range(0,len(parsed_command[3])):
                ora_connect_test(parsed_command[0][0],parsed_command[1][0],parsed_command[2][0] ,parsed_command[3][i][0] , parsed_command[3][i][1] )
    return


def oracle_version(args):
    parsed_command=parse_ping(args+" ;")
    print(parsed_command)
    return


# oracle_sid_test( "192.200.11.9",1521,"DB3")

def oracle_sid_test(p_servername,p_port,p_sid):   

# Check for SID


    byte_msg=bytearray(
       "(DESCRIPTION=(CONNECT_DATA=(SERVER=DEDICATED)(SID="
       +p_sid+
       ")(CID=(PROGRAM=sqlplus)(HOST=anil)(USER=oracle)))(ADDRESS=(PROTOCOL=TCP)(HOST="
       +p_servername+
       ")(PORT="
       +str(p_port)+
       ")))"
    ,  'utf-8')


# TNS Header

    tns_msg1=bytearray([
        0x00, 0x00,                     # Paket Check Sum are not generated by default and left as 0s.
        0x01,                           # type 01 means Connect
	0x00, 				# Reserved
	0x00, 0x00 ,      		# Header checksum always 0
	0x01, 0x34, 			# Version
	0x01, 0x2c, 			# Compatible
	0x00, 0x00, 			# Service Options
	0x08, 0x00, 			# Session Data Unit
	0x7f, 0xff, 			# Max Transation Data Unit Sizeza
	0x4f, 0x98, 			# Nt Protocol Characteristics 
	0x00, 0x00, 			# Line turnaround Value 
	0x00, 0x01,                     # Value of 1 in Hardware
    0x00			        # Length of Connect Data , First Byte
	])

    tns_msg2=bytearray([
	0x00, 0x22, 			# Offset to connect data
	0x00, 0x00, 0x00, 0x00,         # Max Receviable Connect Data
	0x01, 				# Connect Flag 0
	0x01	])                      # Connect Flag 1

    header_msg=tns_msg1+bytearray([len(byte_msg)])+tns_msg2 # TNS Header Connect Part

    total_msg=header_msg+byte_msg           # Full TNS packet except Packet Length

    length_message=len(total_msg)+2         # Length of the full byte includes firts two bytes

    two_bytes=bytearray([0x00])+ bytearray([length_message])  # Firts two byte of the tns packet

    full_tns_packet=two_bytes+total_msg


    sock= socket.socket() 
    sock.settimeout(5)
    try:
        print('')
        print (' Connection : '+p_servername+' : '+str(p_port)+'...')
        sock.connect((p_servername, p_port))
    except Exception as error:
        print("")
        print('  Not Connected to Server ' + str(error))
        print("")
        sock.close()
        return
    print('  Connected to the port')	

    sock.send(full_tns_packet)

    correct_returned_message=bytearray([ 0x00,0x08,0x00,0x00,0x0b,0x00,0x00,0x00])
    
    msg = sock.recv(2048)
    if msg == correct_returned_message:
        print ('>>> '+p_sid+' services on this server as SID <<< SID FOUND ')
    else:
        print ('    '+p_sid+' does not service on this server as SID')
         
        
    sock.close()


# Check for SERVICE_NAME


    byte_msg=bytearray(
       "(DESCRIPTION=(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME="
       +p_sid+
       ")(CID=(PROGRAM=sqlplus)(HOST=anil)(USER=oracle)))(ADDRESS=(PROTOCOL=TCP)(HOST="
       +p_servername+
       ")(PORT="
       +str(p_port)+
       ")))"
    ,  'utf-8')


# TNS Header

    tns_msg1=bytearray([
        0x00, 0x00,            	        # Paket Check Sum are not generated by default and left as 0s.
        0x01,                  	        # type 01 means Connect
	0x00, 				# Reserved
	0x00, 0x00 ,      		# Header checksum always 0
	0x01, 0x34, 			# Version
	0x01, 0x2c, 			# Compatible
	0x00, 0x00, 			# Service Options
	0x08, 0x00, 			# Session Data Unit
	0x7f, 0xff, 			# Max Transation Data Unit Sizeza
	0x4f, 0x98, 			# Nt Protocol Characteristics 
	0x00, 0x00, 			# Line turnaround Value 
	0x00, 0x01,                     # Value of 1 in Hardware
    0x00			        # Length of Connect Data , First Byte
	])

    tns_msg2=bytearray([
	0x00, 0x22, 			# Offset to connect data
	0x00, 0x00, 0x00, 0x00,         # Max Receviable Connect Data
	0x01, 				# Connect Flag 0
	0x01	])                      # Connect Flag 1

    header_msg=tns_msg1+bytearray([len(byte_msg)])+tns_msg2 # TNS Header Connect Part

    total_msg=header_msg+byte_msg           # Full TNS packet except Packet Length

    length_message=len(total_msg)+2         # Length of the full byte includes firts two bytes

    two_bytes=bytearray([0x00])+ bytearray([length_message])  # Firts two byte of the tns packet

    full_tns_packet=two_bytes+total_msg


    sock= socket.socket() 
    sock.settimeout(5)
    try:
        sock.connect((p_servername, p_port))
    except Exception as error:
        print("")
        print('  Not Connected to Server ' + str(error))
        print("")
        sock.close()
        return

    sock.send(full_tns_packet)

    correct_returned_message=bytearray([ 0x00,0x08,0x00,0x00,0x0b,0x00,0x00,0x00])
    
    msg = sock.recv(2048)
    if msg == correct_returned_message:
        print ('>>> '+p_sid+' services on this server as SERVICE_NAME <<< SERVICE_NAME FOUND')
    else:
        print ('    '+p_sid+' does not service on this server as SERVICE_NAME')
         
    sock.close()

    print('')
    return


def ora_connect_test( p_server,p_port,p_sid,p_user,p_passwd):
    print(" ")
    print (' Connection Test: '+p_server+';'+str(p_port)+';'+p_sid+';'+p_user+';'+p_passwd)
    try:
        dsn_tns = cx_Oracle.makedsn(p_server , p_port, p_sid)
        connection = cx_Oracle.Connection(p_user,p_passwd,dsn_tns)
    except Exception as error:
        print("")
        print('  Not Connected to Oracle ' + str(error) )
        print("")
        return
    print(' Connection is Successfull DB version ',connection.version)
    connection.close
    return
