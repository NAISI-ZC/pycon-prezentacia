*** Settings ***
Library    Espresso.CoffeeBeans

*** Test Cases ***
Make Default Coffee
    ${cup_of_coffee}=    Make Cup Of Coffee
    Log To Console    \n\n${cup_of_coffee}

Set Mocha and Make Coffee
    Set Coffee Type    Mocha
    ${cup_of_coffee}=    Make Cup Of Coffee
    Log To Console    \n\n${cup_of_coffee}

Just Make Me Coffee
    ${cup_of_coffee}=    Make Cup Of Coffee
    Log To Console    \n\n${cup_of_coffee}

