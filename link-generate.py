#!/usr/bin/python

# Import the Universe
import sys
import itertools
import time

def slug_generate(chartype):
	"""
		Take a list of character types as an argument. 
		Generate link slugs based on type.
	"""
	print("Generating links....")
	time.sleep(2)
	with open('testlinks.txt', 'a+') as fh: 
		for a, b, c, d, e, f in itertools.product(chartype, chartype, chartype, chartype, chartype, chartype):
			link = a + b + c + d + e + f
			print(link)
			fh.write(link + '\n')
	fh.close()

choice = ""

def print_menu():
	"""
		Prints menu options and exits
	"""
	print(30 * '-')
	print("Is.Gd Slug Generator")
	print(30 * '-')
	print("is.gd generates a 6 character slug when shortening URLs.")
	print("[1]: complete list (very long and not recommended)")
	print("[2]: lowercase list (includes numbers in the generation)")
	print("[3]: word pronouncable (ie ababab) DEFAULT")
	print("[4]: numbers only (very unlikely to be productive)")
	print("[5]: all caps (very unlikely to be productive)")

# Constants
numbers = ['0','1','2','3','4','5','6','7','8','9']
consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
Cons = [c.upper() for c in consonents]
Vows = [v.upper() for v in vowels]
caps = Cons + Vows
lowernums = consonents + vowels + numbers
wordpronounce = consonents + vowels
complete = numbers + consonents + vowels + Cons + Vows


print_menu()
choice = raw_input("Select the type of link to generate: ")
choice = str(choice)

if choice == "1":
	slug_generate(complete)
elif choice == "2":
	slug_generate(lowernums)
elif choice == "3":
	for c1, v1, c2, v2, c3, v3 in itertools.product(consonents, vowels, consonents, vowels, consonents, vowels):
		print(c1 + v1 + c2 + v2 + c3 + v3)
	for v1, c1, v2, c2, v3, c3 in itertools.product(vowels, consonents, vowels, consonents, vowels, consonents):
		print(v1 + c1 + v2 + c2 + v3 + c3)
elif choice == "4":
	slug_generate(numbers)
elif choice == "5":
	slug_generate(caps)
else:
	print("You did not make a selection!")
