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
