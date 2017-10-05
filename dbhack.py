"""

ora_chk -s 192.200.11.9  -p 1521
ora_chk -s 192.200.11.9 , 192.200.11.10  -p 1605
ora_chk -s 192.200.11.9 , 192.200.11.10 , a1.com  -p 1605
ora_chk -s  192.200.11.9-10  -p  1521


"""
from dbhack_parser import *
import os
from dbhack_OracleModules import *
from cmd2 import Cmd
from dbhack_mssqlModules import *
import pyparsing

class REPL(Cmd):


   

    prompt = "dbhack> "
    
    
    
    def __init__(self):

        self.commentGrammars = pyparsing.Or([pyparsing.cStyleComment])
        Cmd.__init__(self)

    def do_commands(self,args):
        " Prints used command names , type help commandname for more information "
        print(' ORACLE Commands ')
        print(' --> ora_chk -s servernames -p ports')
        print(' --> ora_sid -s servernames -p ports -sid sid_names | -sid_file sid_filename')
        print(' --> ora_brute -s servernames  -p ports  -sid sid_names -user usernames | - user_file username_list_file -passwd passwords | -passwd_file password_list_file')
        print(' --> ora_brute_file -s servername  -p port  -sid sid_name  -cred_file username_password_list_file')
        print(' MSSQL Commands ')
        print(' --> mssql_chk -s servernames -p ports')
        print(' --> mssql_brute -s servernames  -p ports  -db sid_name -user usernames | - user_file username_list_file -passwd passwords | -passwd_file password_list_file')
        
         
        

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

    def do_mssql_chk (self,args):

        # ora_chk -s 192.200.11.9  -p 1521
        # ora_chk -s 192.200.11.9 , 192.200.11.10  -p 1605
        # ora_chk -s 192.200.11.9 , 192.200.11.10 , a1.com  -p 1605
        # ora_chk -s  192.200.11.9-10  -p  1521
        # ora_chk -s  atlas.sys.yapikredi.com.tr  -p  1500
        
        """ mssql_chk ping a server to check MS SQL
            mssql_chk -s  servename1,servername2    
            ora_chk -s  192.200.11.9-11   
        """
        mssql_chk(args)

    def do_ora_sid (self,args):

        """ ora_chk_sid chekh sid name on a server
        ora_sid -s servername_list ,-p  port_number_list , -sid sid_name_list | -sid_file file_name  
        ora_sid -s 192.200.11.9  -p 1521 -sid DB3
        ora_sid -s 192.200.11.9  -p 1521 -sid_file D:/x/python/workfile.txt  
        """
        ora_chk_sid(args)

    def do_ora_brute (self,args):

        """ ora_connect tries to connect ORacle database
        ora_brute -s servername_list ,-p  port_number_list , -sid sid_name_list -user usernames -password passwords   
        ora_brute -s 192.200.11.9  -p 1521 -sid DB3 -user SYSTEM -passwd ORACLE
          
        """
        ora_connect(args)
        
    def do_mssql_brute (self,args):

        """ ora_connect tries to connect ORacle database
        ora_brute -s servername_list ,-p  port_number_list , -db sid_name_list -user usernames -password passwords   
        ora_brute -s 192.200.11.9  -p 1521 -db DB3 -user SYSTEM -passwd ORACLE
        
        """
        mssql_connect(args)


    def do_ora_brute_file (self,args):

        """ ora_connect tries to connect ORacle database
        ora_brute_file -s servername_list ,-p  port_number_list , -sid sid_name  -cred_file D:/x/python/cred-file.txt   
        ora_brute_file -s server -p 1632 -sid fdssdg -cred_file D:/x/python/cred-file.txt
        ora_brute_file -s 192.200.11.9  -p 1521 -sid DB3 -cred_file D:/x/python/cred-file.txt  
        """
        ora_brute_with_file(args)
        
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
    print(' --> Current Commands')
    print(' --> ****************')
    print(' --> ora_chk')
    print(' --> ora_chk_sid')
    print(' ')
    print(' Type help CommandName to get much more information')
    print(' ')
    app = REPL()
    app.cmdloop()
