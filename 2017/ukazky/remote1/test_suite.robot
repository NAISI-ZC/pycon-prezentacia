*** Settings ***
Library    Remote    192.168.0.104:2347

*** Test Cases ***
Test Remote Coffee Machine
    ${cup_of_coffee}=    Make Cup Of Coffee    Black
    Log To Console    \n\n${cup_of_coffee}
