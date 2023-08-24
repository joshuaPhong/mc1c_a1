# MC1C-A1: Assignment one for python micro-credential
# Project Description
This project is for the Python Micro-Credential by WhiteCliffe.
This readme is as much for the marker as it is for any dev who uses the code.
## Assignment Brief
Use OOP Python to meet the client's brief. 
* Provide the required functionality.
* The unit tests to prove functionality. 
* Document the code.
## Customers Senario
The client, CloudX, requires that their online shopping cart be updated to include a Black Friday discount. All customers who met the following conditions will get a black friday discount. The cart has at least five items in it, and the customer spends at least $200.00.
# Summary - How I met the brief
## Using OOP principles
In this assignment I was able to impliment the following OOP priciples.
* Classes. I created a class BlackFriday. It contains a private variable and a discount method.
* Objects. I have used objects in the main.py and test_black_friday.py. Primarily for testing purposes. Instantiating Objects for both Unit tests and White Box tests.
These objects, have states (the values passed), behaviour (the method used) and, an identity (the objects name).  
* Encapsulation. All class methods and variables relating to the black friday sale are wrapped in the black friday class.
I have used a private class variable for the discount value. The methods in the class can use it but it cannot be accessed from outside the class i.e. by its objects.
# How to
## Create an object
import the the module. 
import black_friday
object_name = black_friday.BlackFriday()
or, alternativly,
from black_friday import BlackFriday
object_name = BlackFriday()
## Use the object / access the method
object_name.method_name(arg1,arg2). See main.py for examples.
# Tests
I tested in two ways.
I constructed unittests and I instantiated objects and passed arguments to the method to record the console output.
## Unit tests
Testing the function with varying inputs / test data
All unit tests are in test_black_friday.py
Using pycharm I first constructed a stub when creating the test_ file.
This imports the unit test module, creates a TestClass, and a test method. These were appropriately renamed. 
I imported the black_friday.py file to be tested.
I then began constructing individual unit tests. I used individual unit tests because they are clearer, more readable, and they all use different test data.
First a docstring, a short description of what was being tested.
Then I followed a given, when, then model. Given a set of test data (create the data), when we call the function (call the function with the test data), then impliment the test (an assertEqual in all cases). Result, Pass or Fail.
I tested for; minimum conditions, exceed conditions, below conditions, one condition True and the other False, edges, zeros, large numbers, negative numbers, and strings.
## Whitebox tests
Instantiating an object of class BlackFriday and using it while passing a variety of arguments to it. Compared the output to expected results.
These tests can be found in main.py and the output / results can be seen in the console by running main.py

# Sources
See black_friday.py and test_black_friday.py for sources used relevant to each file.

