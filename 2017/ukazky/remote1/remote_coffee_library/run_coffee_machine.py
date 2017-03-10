from robotremoteserver import RobotRemoteServer

class Espresso:
    def make_cup_of_coffee(self, type_of_coffee):
        cup = self._pour_coffee(type_of_coffee)
        return cup

    def _pour_coffee(self, type_of_coffee):
        return """
             (
              ) (
             (   ) 
           ,-------.
          c|       |
           | {} |
           |       |
           =========
 """.format(type_of_coffee)


########################

def main():
    lib = Espresso()

    # run server indefinitely
    try:
        server = RobotRemoteServer(lib, '0.0.0.0', 2347)
    except KeyboardInterrupt, e:
        log("INFO: Keyboard Iterrupt: stopping server")
        server.stop_remote_server()

if __name__ == "__main__":
    main()
