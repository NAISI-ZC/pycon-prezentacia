This is same example as before, but this time, we are dealing with statefull
library. It means that RF keeps instance of this library in some scope and
we can access it's internal state (some variable for example)

There are 3 types of scope in RF. `TEST_CASE`, `TEST_SUITE` and `GLOBAL`.

 * TEST_CASE - RF will create new instance of library for each test case
 * TEST_SUITE - RF will create new instance of library for each test suite
 * GLOBAL - RF will keep only 1 instance during whole execution


Scope has to be set in python library itself. It must contains variable with
name `ROBOT_LIBRARY_SCOPE`

    class Espresso:
        ROBOT_LIBRARY_SCOPE = 'TEST_CASE'
    
        def __init__(self):
            self._type_of_coffee = "Black"

        def make_cup_of_coffee(self):
            cup = self._pour_coffee()
            return cup


