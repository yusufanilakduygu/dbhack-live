import os
# import .\OracleModules

from cmd2 import Cmd


class REPL(Cmd):

    redirector = '->'

    prompt = "dbhack> "
    intro = "Welcome to the real world!"

    def __init__(self):
        Cmd.__init__(self)

    def do_status(self, args):
        print(len(args))
        for x in range(len(args)):
            print(args[x])
            
    def do_tnsping (self,args):
        tnsping(args)


if __name__ == '__main__':
    app = REPL()
    app.cmdloop()
