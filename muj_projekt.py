"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Jirásko
email: ma.jirasko@gmail.com
discord: Martin J#3568
"""

'''
author = Martin Jirásko
'''
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

# registrovani uzivatele
registrovani= {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

rg_jmena = ("bob", "ann", "mike", "liz")
rg_hesla = ("123", "pass123", "password123", "pass123")

# zadani prihlasovacich udaju
pr_jmeno = input("Username: ")
pr_heslo = input("Userpassword: ")

if (pr_jmeno not in rg_jmena) or (registrovani.get(pr_jmeno) != pr_heslo):
  print("unregistred user, terminating the program...")
  quit()
else:
  print(f"Welcome to the app, {pr_jmeno}. \nWe have 3 texts to be analyzed:")


print("-" * 50)
# vytiskne dostupne texty
for i, prvek in enumerate(TEXTS, start=1):
    print(f"{i}. {prvek}")

print("-" * 50)

# vybere text
cislo = int(input("Enter a number: "))
vybrany_text = TEXTS[cislo - 1].split()

if cislo >= 1 and cislo <= 3:
    print("Start analyzing")
else:
    print("Enter a valid number.")

# vytiskne vybrany text
print("-" * 50)

print(TEXTS[cislo - 1])

print("-" * 50)

# pocet slov
pocet_slov = len(vybrany_text)

print(f"There are {pocet_slov} words in the selected text.")

# pocet slov zacinajici velkym pismenem
pocet_slov = list()

for slovo in vybrany_text:
    if slovo.istitle():
        pocet_slov.append(slovo)

pocet_velkych = len(pocet_slov)
print(f"There are {pocet_velkych} titlecase words.")

# pocet slov psanych velkymi pismeny
velka_slova = list()

for slovo in vybrany_text:
    if slovo.isupper():
        velka_slova.append(slovo)

pocet_velkych_slov = len(velka_slova)
print(f"There are {pocet_velkych_slov} uppercase words.")

# počet slov psanych malymi pismeny
mala_slova = list()

for slovo in vybrany_text:
    if slovo.islower():
        mala_slova.append(slovo)

pocet_malych_slov = len(mala_slova)
print(f"There are {pocet_malych_slov} lowercase words.")

# počet čísel
cisla = list()

for slovo in vybrany_text:
    if slovo.isnumeric():
        cisla.append(slovo)

pocet_cisel = len(cisla)
print(f"There are {pocet_cisel} numeric strings.")

# suma všech čísel (ne cifer) v textu
soucet = 0

for slovo in vybrany_text:
    if isinstance(slovo, int) or slovo.isdigit():
        soucet += int(slovo)
print(f"The sum of all the numbers {soucet}")

print("-" * 50)


# vytvori sloupcovy graf
ocislovani = 0

for slovo in vybrany_text:
    delka_slova = len(slovo)
    pocet_hvezd = "*" * delka_slova
    ocislovani += 1
    print(ocislovani, "|", pocet_hvezd, "|", delka_slova)











