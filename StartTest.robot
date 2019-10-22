*** Settings ***
Library           OperatingSystem
Library           WinExeControlLibrary.py
Library           Process

*** Test Cases ***
Test string.exe With Self Library
     Send cmd    test
     Status should be    String Test

Test string.exe With Process Library
     ${result} =    Run Process    string.exe
     Should Match    ${result.stdout}    String Test
