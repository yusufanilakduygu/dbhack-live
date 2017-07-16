import os
from OracleModules import *

from cmd2 import Cmd


class REPL(Cmd):

   

    prompt = "dbhack> "
    intro = "dbhack program ver 1.2 Developed by Y. Anıl Akduygu Sile/Istanbul"

    def __init__(self):
        Cmd.__init__(self)

    def do_oracle_ping(self,args):
        oracle_ping(args)

    def do_oracle_version(self,args):
        oracle_version(args)


if __name__ == '__main__':
    print(parse_ping("-server x, y   -port 123-67; "))
    app = REPL()
    app.cmdloop()
