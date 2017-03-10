import inspect

def keyword(func):
    '''Decorator will add attribute "robot" into function
    This information is later use to select which methods are keywords and which
    are only methods.
    '''
    func.robot = True
    return func

class RobotBaseClass(object):
    """Base class implementing common methods for robot framework Dynamic API"""

    def get_keyword_names(self):
        '''This method will examine "self" and will go through all instance
        methods. Only methods which has "robot" attribute.
        
        This list is then supplied back to RF as strings (names of keywords)
        '''
        return [name for name in dir(self) if hasattr(getattr(self, name), 'robot')]

    def get_keyword_arguments(self, kw_name):
        '''This method will be used by RF to check what arguments keyword
        accepts. RF will use keyword names which we've supplied in previous
        method.

        Following code will get function object from "self" and use inspect
        module, to inspect arguments of this functions. This information is
        then supplied in format that RF understands.
        '''
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

