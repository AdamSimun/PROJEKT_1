"""
PROJEKT_1.py: první projekt do Engeto Online Python Akademie

author: Adam Šimůnek
email: adam.simunek@seznam.cz
discord: -
"""

#help
separator = "-"*54

#entrance variables - texts to be analyzed
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


#entrance variables - login
log_in = dict()
log_in["bob"] = "123"
log_in["ann"] = "pass123"
log_in["mike"] = "password123"
log_in["liz"] = "pass123"

#log-in processa
user_log = input("username: ")
password_log = input("password: ")
print(separator)

if user_log in log_in.keys() and log_in[user_log] == password_log:
    print("Welcome to the app,", user_log, "\nWe have",len(TEXTS), "text to be analyzed")
    print(separator)    
else:
    print("unregistred user, terminating the program")
    quit()

#select text
print("Enter a number btw. 1 and ", str(len(TEXTS)))
selected_number = input("to select: ")

#text index check
if not int(selected_number) in range(1,len(TEXTS)+1): 
    print("selected number does not in range, terminating the program")
elif selected_number.isnumeric() != True:
    print("selected number is not numerical, terminating the program")
else: 
    print(separator)

# cleaning words
words_cleaned = list()
text_split = TEXTS[int(selected_number)].split()
for slovo in text_split:
    slovo = slovo.strip(".!?_:;")
    words_cleaned.append(slovo.lower())
print(words_cleaned)

#statistics - count words in text
#count_words = len(texts_split)










