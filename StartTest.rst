.. default-role:: code

=====================================
  Robot Framework Quick Start Guide
=====================================

.. contents:: Table of contents:
   :local:
   :depth: 2

   Introduction
============

About this guide
----------------

Test cases
==========

Workflow tests
--------------

.. code:: robotframework

    *** Test Cases ***
    Test string.exe With Self Library
         Send cmd    test
         Status should be    String Test

    Test string.exe With Process Library
         ${result} =    Run Process    string.exe
         Should Match    ${result.stdout}    String Test

.. code:: robotframework

    *** Settings ***
    Library           OperatingSystem
    Library           WinExeControlLibrary.py
    Library           Process
