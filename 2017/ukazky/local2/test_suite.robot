*** Settings ***
Library    CoffeeLibrary.Espresso
# Library    Espresso

*** Test Cases ***
Test Coffee Machine
    ${cup_of_coffee}=    Make Cup Of Coffee    Black
    Log To Console    \n\n${cup_of_coffee}
