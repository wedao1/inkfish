import paramiko
from plumbum import cli
import pssh

class MyApp(cli.Application):
    verbose = cli.Flag(["v", "verbose"], help = "Make ssh more powerful")
    name = "" 
    command = ""
    style=""
    @cli.switch("-n", str)
    def set_name(self, name):
        """Set the keyword of name"""
        self.name=name
    
    @cli.switch("-c", str)
    def set_command(self, command):
        """Set the command"""
        self.command=command

    @cli.switch("-s", int)
    def set_style(self, style):
        """Set the style"""
        self.style=style

    def main(self):
        pssh.cmd(self.name,self.command,self.style)
if __name__ == "__main__":
    MyApp.run()
