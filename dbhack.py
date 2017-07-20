"""

oracle_ping -server dsds -port 12
oracle_version -server dsds -port 12

"""
from dbhack_parser import *
import os
from dbhack_OracleModules import *
from cmd2 import Cmd


class REPL(Cmd):

   

    prompt = "dbhack> "

    
    def __init__(self):
        Cmd.__init__(self)

    def do_oracle_ping(self,args):
        """ oracle_ping ping a server to check Oracle database 
            oracle_ping -server servename1,servername2 -port 1454,1455  
            oracle_ping -server 192.168.45.1000-1750   -port 1454-1700
        """
        oracle_ping(args)

    def do_oracle_version(self,args):
        """ oracle_ping version tries to find Oracle database version
            oracle_ping -server servename1,servername2 -port 1454,1455  
            oracle_ping -server 192.168.45.1000-1750   -port 1454-1700
        """
        oracle_version(args)

    def do_commands(self,args):
        " Prints used command names , type help commandname for more information "
        print(' --> oracle_ping')
        print(' --> oracle_version')   


if __name__ == '__main__':
    print(' ')
    print("dbhack program ver 1.2 Developed by Y. Anıl Akduygu Sile/Istanbul")
    print(' You can use below commands')
    print(' --> commands')
    print(' --> oracle_version')
    print(' --> oracle_ping')
    print(' --> oracle_version')
    print(' ')
    print(' Type help CommandName to get much more information')
    print(' ')
    app = REPL()
    app.cmdloop()
