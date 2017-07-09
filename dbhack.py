import os
from BlackBoxTests import OracleModules

from cmd2 import Cmd


class REPL(Cmd):

   

    prompt = "dbhack> "
    intro = "dbhack program ver 1.0 Developed by Y. Anıl Akduygu Sile/Istanbul"

    def __init__(self):
        Cmd.__init__(self)

    def do_tnsping (self,args):
        OracleModules.tnsping(args)

    def do_tnsversion (self,args):
        OracleModules.tnsversion(args)


if __name__ == '__main__':
    app = REPL()
    app.cmdloop()
