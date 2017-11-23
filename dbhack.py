"""
This is the starting code for DBHack

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
        " Below you can see developed command names , type help command_name for more information "
        print(' ORACLE Commands ')
        print(' --> ora_chk ')
        print(' --> ora_sid  ')
        print(' --> ora_brute -s servernames  -p ports  -sid sid_names -user usernames | - user_file username_list_file -passwd passwords | -passwd_file password_list_file')
        print(' --> ora_brute_file -s servername  -p port  -sid sid_name  -cred_file username_password_list_file')
        print(' MSSQL Commands ')
        print(' --> mssql_chk -s servernames ')
        print(' --> mssql_brute -s servernames  -p ports  -db sid_name -user usernames | - user_file username_list_file -passwd passwords | -passwd_file password_list_file')
        

    def do_ora_chk (self,args):

        """

        Command Name : ora_chk
​
        Explanation
        ----------
        ora_chk pings a server with ports to check Oracle databases
        This command pings a server or servers or a network range
        Port can be a single port or ports or a port range
        Syntax
        ----------
        ora_chk -s  <servename1,servername2,...>  -p  <port01,port02 ...>
        ora_chk -s  < xxx.xxx.xxxx.xx-xxx> -p < port01-port02>
        Samples
        ---------
        ora_chk -s 192.168.0.27 -p 1521
        ora_chk -s 192.168.0.27 -p 1521-1522
        ora_chk -s 192.168.0.27-28  -p 1521,1522
        ora_chk -s 192.168.0.27, 192.168.15.28  -p 1521,1522
        ora_chk -s 192.168.0.27-30  -p 1521,1522
        ora_chk -s servername01  -p 1521,1522
        ora_chk -s servername01,servername01  -p 1521,1522

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

        """

        Command Name : ora_sid
​
        Explanation
        -----------
        ora_sid tries to guess Oracle SID and SERVICE_NAME
        command first tries given names as a SID  , and then tries the same name  as  a SERVICE_NAME
        You can scan servers and ports as ora_chk command
        SID or SERVICE_NAME names can be given in the command or they can be given in the file
		sid-list.txt file is added as a sample 
		this file is an updated version of http://www.red-database-security.com/scripts/sid.txt

        Syntax
        ----------
        ora_sid -s  <servename1,servername2,...>  -p  <port01,port02 ...> -sid <sid_name_list> | -sid_file <file_name>
        ora_sid -s  < xxx.xxx.xxxx.xx-xxx> -p < port01-port02> -sid <sid_name_list> | -sid_file <file_name>

        Samples
        ---------
        ora_sid -s 192.168.0.27  -p 1521,1522  -sid DB3,DB4
        ora_sid -s 192.168.0.27  -p 1521,1522  -sid_file sid-list.txt 
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

    def do_mssql_brute_null_passwd (self,args):

        """ ora_connect tries to connect ORacle database
            mssql_brute_null_passwd -s server_name -p port -user usernames
   
        
        """
        mssql_connect_null_passwd (args)
        
    def do_mssql_brute_file(self,args):

        """ ora_connect tries to connect ORacle database
        ora_brute -s servername_list ,-p  port_number_list , -db sid_name_list -user usernames -password passwords   
        ora_brute -s 192.200.11.9  -p 1521 -db DB3 -user SYSTEM -passwd ORACLE
        
        """
        mssql_brute_with_file(args)

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
    print("dbhack program ver 1.0 Developed by Y. Anıl Akduygu in Sile/Istanbul")
	print("type help to see all commands 
	print("type help <command_name> to see details about a command")

    print(' You can use below commands')
    print(' --> Current Commands')
    print(' --> ****************')
    print(' --> ora_chk')
    print(' --> ora_sid')
    print(' ')
    print(' Type help CommandName to get much more information')
    print(' ')
    app = REPL()
    app.cmdloop()
