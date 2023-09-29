"""
PROJEKT_1.py: první projekt do Engeto Online Python Akademie

author: Adam Šimůnek
email: adam.simunek@seznam.cz
discord: -
"""

#help
separator = "-"*54

#entrance variables - texts to be analyzed
texts = dict


#entrance variables - login
log_in = dict()
log_in["bob"] = "123"
log_in["ann"] = "pass123"
log_in["mike"] = "password123"
log_in["liz"] = "pass123"

texts

#log-in processa
user_log = input("username: ")
password_log = input("password: ")
print(separator)

if user_log in log_in.keys() and log_in[user_log] == password_log:
    print("Welcome to the app,", user_log, "\n We have 3 text to be analyzed")
    print(separator)    
else:
    print("unregistred user, terminating the program")
    quit()

print()
    


#if log_in[user_log] == password_log:
    #print("Your password is correct.")
#else:
    #print("Sorry", user_log, "but your password is wrong. Application quits.")
    #quit()
    
print("Welcome to our text-analyse application.")

