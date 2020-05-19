#!/bin/python

import random
chars ='abcdefghijklmopqrstuvwxyz1234567890ABCDEFGHIJKLMOPQRSTUVWXYZ!@'
number = input('How many password would you like to generate? - ')
number = int(number)
length = input('how many chracters would you like your password to be? - ')
length =int(length)
for p in range (number):
    password = ' '
    for c in range(length) : 
        password += random.choice(chars)
        print(password)

