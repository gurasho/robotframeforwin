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
    User can create a Cat
      Send cmd    test
      Status should be    String Test

.. code:: robotframework

    *** Settings ***
    Library           OperatingSystem
    Library           WinExeControlLibrary.py
  
User keywords
-------------
.. code:: robotframework

    *** Keywords ***
    Clear login database
        Remove file    ${DATABASE FILE}

    Create valid user
        [Arguments]    ${username}    ${password}
        Create cat    ${username}    ${password}
        Status should be    SUCCESS
