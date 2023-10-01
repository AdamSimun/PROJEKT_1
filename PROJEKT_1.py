"""
PROJEKT_1.py: první projekt do Engeto Online Python Akademie

author: Adam Šimůnek
email: adam.simunek@seznam.cz
discord: adamsim2
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


#entrance variables - login data
log_in = dict()
log_in["bob"] = "123"
log_in["ann"] = "pass123"
log_in["mike"] = "password123"
log_in["liz"] = "pass123"

#login check
user_log = input("username: ")
password_log = input("password: ")
print(separator)

if user_log in log_in.keys() and log_in[user_log] == password_log:
    print(f"Welcome to the app, {user_log}", f"We have {len(TEXTS)} text to be analyzed.", separator, sep="\n")   
else:
    print("unregistred user, terminating the program")
    quit()

#select text
print(f"Enter a number btw. 1 and {len(TEXTS)}")
selected_number = input("to select: ")

#selected text-index check
if selected_number.isnumeric() != True:
    print("selected number is not numerical, terminating the program")
    quit()
elif not int(selected_number) in range(1,len(TEXTS)+1): 
    print("selected number does not in range, terminating the program")
    quit()
else: 
    print(separator)

# words cleaning
words_cleaned = list()
text_split = TEXTS[int(selected_number)-1].split()
for word in text_split:
    word = word.strip(".!?_:;,")
    words_cleaned.append(word)

#statistics - count words in text
words_titlecase = list()
words_uppercase = list()
words_lowercase = list()
numeric = list()

for word2 in words_cleaned:
    if word2.istitle():
        words_titlecase.append(word2)
    elif word2.isupper():
        words_uppercase.append(word2)
    elif word2.islower():
        words_lowercase.append(word2)
    elif word2.isnumeric:
        numeric.append(float(word2))
    else:
        continue

print(f"There are {len(words_cleaned)} words in the selected text.")     
print(f"There are {len(words_titlecase)} titlecase words")
print(f"There are {len(words_uppercase)} uppercase words")
print(f"There are {len(words_lowercase)} lowercase words")
print(f"There are {len(numeric)} numeric strings")
print(f"The sum of all the numbers: {sum(numeric)}")
print(separator)

#plot - max length word
words_length = list()
for word3 in words_cleaned:
    words_length.append(len(word3))

word_max_length = max(words_length)
plot_len_range = list(range(1,(word_max_length+1)))

dict_len_words = dict()
for rank in plot_len_range:
    dict_len_words[rank] = 0

#plot - count words by their length
for word4 in words_cleaned:
    dict_len_words[len(word4)] = dict_len_words[len(word4)] + 1

#plot - graphic
plot_labels = ("LEN", "OCCURENCES", "NR.")
occurences_len = max(dict_len_words.values())

print(f"{plot_labels[0].center(4)}|{plot_labels[1].center(occurences_len+5)}|{plot_labels[2].ljust(10)}", separator, sep="\n")
for key in dict_len_words:
    print(f"{str(key).center(4)}|{str((dict_len_words[key])*'*').ljust(occurences_len+5)}|{str(dict_len_words[key]).ljust(10)}")


























