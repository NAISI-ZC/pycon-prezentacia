*** Settings ***
# Library    coffee_library
Library    coffee_library.py

*** Test Cases ***
Check Coffee Machine
    ${coffee_status}=    Get Coffee Machine Status
    Log To Console    \n\n\t\t${coffee_status}\n

