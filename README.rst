.. default-role:: code

=====================================
  Robot Framework Test
=====================================

Introduction
--------------
| 自作のキーワードと、Processライブラリのキーワードで同様のことができるかの比較
| テスト内容は、"string test"を出力するexeを実行し、期待値かどうかを判別する
| 
| このファイル自体が実行ファイルとなっており、下記で実行可能
| >robot README.rst


Test
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
