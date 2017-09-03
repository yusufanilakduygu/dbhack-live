"""

ora_chk -s 192.200.11.9  -p 1521
ora_chk -s 192.200.11.9 , 192.200.11.10  -p 1605
ora_chk -s 192.200.11.9 , 192.200.11.10 , a1.com  -p 1605
ora_chk -s  192.200.11.9-10  -p  1521

ora_chk  -s  atlas.sys.yapikredi.com.tr  -p  1500-1510

"""
from dbhack_parser import *
import os
from dbhack_OracleModules import *
from cmd2 import Cmd


class REPL(Cmd):

   

    prompt = "dbhack> "

    
    def __init__(self):
        Cmd.__init__(self)

    def do_ora_chk (self,args):

        # ora_chk -s 192.200.11.9  -p 1521
        # ora_chk -s 192.200.11.9 , 192.200.11.10  -p 1605
        # ora_chk -s 192.200.11.9 , 192.200.11.10 , a1.com  -p 1605
        # ora_chk -s  192.200.11.9-10  -p  1521
        # ora_chk -s  atlas.sys.yapikredi.com.tr  -p  1500
        
        """ ora_chk ping a server to check Oracle database 
            ora_chk -s  servename1,servername2 -p  1454,1455  
            ora_chk -s  192.200.11.9-11   -p  1521-1522
        """
        ora_chk(args)

    def do_ora_chk_sid (self,args):

        """ ora_chk_sid chekh sid name on a server
        ora_chk_sid -s servername_list ,-p  port_number_list , -sid sid_name_list | -sid_file file_name  
        ora_chk_sid -s 192.200.11.9  -p 1521 -sid DB3
        ora_chk_sid -s 192.200.11.9  -p 1521 -sid_file D:/x/python/workfile.txt  
        """
        ora_chk_sid(args)


    def do_commands(self,args):
        " Prints used command names , type help commandname for more information "
        print(' --> ora_chk -s [servernames] -p [ports]')


    def do_version(self,args):
        print('')
        print(" dbhack ver 1.0 Developed bu Y. Anıl Akduygu at Sile/Istanbul ")
        print(" ")

    def do_exit(self,args):
        exit()

if __name__ == '__main__':
    print(' ')
    print("dbhack program ver 1.0 Developed by Y. Anıl Akduygu Sile/Istanbul")
    print(' You can use below commands')
    print(' --> commands')
    print(' --> ora_chk')
    print(' ')
    print(' Type help CommandName to get much more information')
    print(' ')
    app = REPL()
    app.cmdloop()
