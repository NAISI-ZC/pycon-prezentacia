import inspect

def keyword(func):
    func.robot = True
    return func

class RobotBaseClass(object):
    """Base class implementing common methods for robot framework api"""

    def get_keyword_names(self):
        return [name for name in dir(self) if hasattr(getattr(self, name), 'robot')]

    def get_keyword_arguments(self, kw_name):
        kw = getattr(self, kw_name)
        args, _, _, defaults = inspect.getargspec(kw)
        args = filter(lambda x: x != 'self', args)
        if defaults:
            default_args = args[-len(defaults):]
            default_args = [default_args[i] + '=' + str(defaults[i])
                    for i in range(len(defaults))]
            args = args[0:-len(defaults)] + default_args
        return args

    def run_keyword(self, name, args):
        keyword = getattr(self, name)
        return keyword(*args)

class CoffeeBeans(RobotBaseClass):
    ROBOT_LIBRARY_SCOPE = 'TEST_CASE'
    # ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, type_of_coffee='Black'):
        self._type_of_coffee = type_of_coffee

    @keyword
    def set_coffee_type(self, type_of_coffee):
        self._type_of_coffee = type_of_coffee

    @keyword
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

