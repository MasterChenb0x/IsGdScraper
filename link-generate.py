#!/use/bin/env python

# Import the world
import sys
import itertools
# Initialization
consonent = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

vowel = ['a','e','i','o','u']

# Print desired combinations starting with consonents
for c1, v1, c2, v2, c3, v3 in itertools.product(consonent, vowel, consonent, vowel, consonent, vowel):
	print(c1 + v1 + c2 + v2 + c3 + v3)


# Print desired combinations starting with vowels
for v1, c1, c2, v2, c3, v3 in itertools.product(vowel, consonent, vowel, consonent, vowel, consonent):
	print(v1 + c1 + v2 + c2 + v3 + c3)

