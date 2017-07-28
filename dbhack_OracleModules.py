
from dbhack_parser import *
import socket
import itertools


def tns_ping(p_servername,p_port):
    sock= socket.socket() 
    try:
        print('')
        print (' Connection : '+p_servername+' : '+str(p_port)+'...', end="")
        sock.connect((p_servername, p_port))
    except Exception:
        print('not connected')
        print('')
        sock.close()
        return
    print('CONNECTED')	
 
    
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

    sock.send(send_msg)
    msg = sock.recv(2048)
    sock.close()
    decoded_msg=msg.decode('ascii')
    i=decoded_msg.find('ERR=0')
    if i != -1:
        print ("   Oracle Listener Found  ...",end="")  
        print('Listener Name : ',msg.decode('ascii')[msg.decode('ascii').find("ALIAS=")+6:-2])
        print()
    else:
        print ("Oracle Listener Not Found")
        print()
    return

def oracle_analyze(args):
    parsed_command=parse_ping(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0], parsed_command[1]):
                tns_ping(i[0],i[1])
    return


def oracle_version(args):
    parsed_command=parse_ping(args+" ;")
    print(parsed_command)
    return
