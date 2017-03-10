This python module contains python class which is instatiated in RF and
keywords are imported from this class.

In order to import library in RF, you have to specify `--pythonpath .` and
use module name and class name when importing.

    *** Settings ***
    Library    CoffeeLibrary.Espresso

If you want to simplify the import, use same filename and class name. In this
case, rename module `CoffeeLibrary.py` to `Espresso.py` and simply import
library in RF with following

    *** Settings ***
    Library    Espresso


It's good to use python class, when we have more complex test library with
multiple classses, abstract classes, inheritance, etc.

