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
* Encapsulation. All methods and attributes relating to the black friday sale are wrapped in the black friday class.
I have used a private class variable for the discount value. The methods in the class can use it but it cannot be accessed from outside the class.
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

# Sources
[Link] (https://www.geeksforgeeks.org/python-oops-concepts/)

