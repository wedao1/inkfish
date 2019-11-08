import paramiko
from plumbum import cli
class MyApp(cli.Application):
    verbose = cli.Flag(["v", "verbose"], help = "If given, I will be very talkative")
    def main(self, filename):
        print("I will now read {0}".format(filename))
        if self.verbose:
            print("Yadda " * 200)
if __name__ == "__main__":
    MyApp.run()
