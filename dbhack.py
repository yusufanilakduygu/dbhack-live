"""

oracle_analyze -server 192.200.11.9  -port 1521
oracle_analyze  -server 10.51.16.27  -port 1605
oracle_analyze -server 192.200.11.9  -port 1521

oracle_ping  -server atlas.sys.yapikredi.com.tr  -port 1500-1510

"""
from dbhack_parser import *
import os
from dbhack_OracleModules import *
from cmd2 import Cmd


class REPL(Cmd):

   

    prompt = "dbhack> "

    
    def __init__(self):
        Cmd.__init__(self)

    def do_ora_chk(self,args):
        """ ora_chk ping a server to check Oracle database 
            ora_chk -s  servename1,servername2 -p  1454,1455  
            ora_chk -s  192.168.45.1000-1750   -p  1454-1700
        """
        oracle_analyze(args)


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
