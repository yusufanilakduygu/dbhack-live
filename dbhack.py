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
        print(' --> ora_brute ')
        print(' --> ora_brute_file  ')
        print(' MSSQL Commands ')
        print(' --> mssql_chk -  ')
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

    def do_mssql_chk_browser (self,args):
       
        """ 

        Command Name : mssql_chk_browser
​
        Explanation
        ----------
        mssql_chk_browser pings SQL Server Browser in any server.
	This command is used to know if the SQL server is running on a server.
	If SQL Server does nor respond to your request. It does not mean that
	SQL server is not running on this server. 

        Syntax
        ----------
        mssql_chk_browser  <server1,server2> 
        mssql_chk_browser -s  < xxx.xxx.xxxx.xx-xxx>  

        Samples
        ---------
        mssql_chk_browser -s 192.168.1.37  
        mssql_chk_browser -s 192.168.1.37-40
	mssql_chk_browser -s 192.168.1.37, 192.168.1.42
   
        """
        mssql_chk(args)



    def do_ora_sid (self,args):

        """

        Command Name : ora_sid
​
        Explanation
        -----------
        ora_sid tries to guess Oracle SID and SERVICE_NAME
        command first tries given names as a SID to guess SID 
	and then tries the same name  as  a SERVICE_NAME to guess service name
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

        """ 
        Command Name : ora_brute
​
        Explanation
        -----------
	ora_brute tries to connect Oracle database 
        with given usernames and passwords,
	Username and password pairs can be given in the command
	At the same time you can use username list file and password list file 

        Syntax
        ----------
        ora_brute -s <servername> ,-p  <port_number> , -sid <sid_name> -user <username_list> -passd <password_list>   
	ora_brute -s <servername> ,-p  <port_number> , -sid <sid_namet> -user_file <usernames-list-file > -passd_file <passwords-list-file>   

        Samples
        ---------
        ora_brute -s 192.168.1.34 -p 1521 -sid DB3 -user system,scott  -passwd oracle,tiger
	ora_brute -s 192.168.1.34 -p 1521 -sid DB3 -user_file username-list.txt -passwd_file passwd-list.txt
          
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

        """ 
        Command Name : ora_brute_file
​
        Explanation
        -----------
	ora_brute tries to connect Oracle database 
        with given ucredential file
	This file contains; Username, Password pairs.

        Syntax
        ----------
        ora_brute_file -s <servername> ,-p  <port_number> , -sid <sid_name> -cred_file  <usercredential_file>   
	  

        Samples
        ---------
        ora_brute_file  -s 192.168.1.34 -p 1521 -sid DB3 -cred_file oracle-cred-file.txt

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
    print(" ")
    print(' You can use below commands')
    print(' --> Current Commands')
    print(' --> ****************')
    print(' --> ora_chk')
    print(' --> ora_sid')
    print(' --> ora_brute')
    print(' ')
    print(' Type help CommandName to get much more information')
    print(' ')
    app = REPL()
    app.cmdloop()
