"""
PROJEKT_1.py: první projekt do Engeto Online Python Akademie

author: Adam Šimůnek
email: adam.simunek@seznam.cz
discord: -
"""

#entrence variables

log_in = dict()
log_in["bob"] = "123"
log_in["ann"] = "pass123"
log_in["mike"] = "password123"
log_in["liz"] = "pass123"

#log-in processa
user_log = input("Write your user's name: ")

if not user_log in log_in.keys():
    print("We are sorry, but your username is not in our database. Application quits.")
    quit()
else:
    print("Your username has been found successfully in our database:")

password_log = input("Write your password: ")

if log_in[user_log] == password_log:
    print("Your password is correct.")
else:
    print("We are sorry, but your password is wrong. Application quits.")
    quit()
    
print("Welcome to our text-analyse application.")

