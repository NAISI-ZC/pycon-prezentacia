This is very basic usage of custom library for robot framework.
Python script is right next to RF (Robot Framework) test script. We have to be
carefull to include location of our python module into python path for RF.


If we use following syntax to import library.

    *** Settings ***
    Library    coffee_library


We can include current directory with RF option `--pythonpath .`
Other solution would be to import library in RF with relative / absolute path.

    *** Settings ***
    Library    ./coffee_library.py


This type of library is stateless. It contains only functions and no internal
state.
