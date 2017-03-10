
class CoffeeBeans(object):

    ROBOT_LIBRARY_SCOPE = 'TEST_CASE'
    # ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, type_of_coffee='Black'):
        self._type_of_coffee = type_of_coffee

    def set_coffee_type(self, type_of_coffee):
        self._type_of_coffee = type_of_coffee

    def make_cup_of_coffee(self):
        cup = self._pour_coffee()
        return cup

    def _pour_coffee(self):
        return """
             (
              ) (
             (   ) 
           ,-------.
          c|       |
           | {} |
           |       |
           =========
 """.format(self._type_of_coffee)
