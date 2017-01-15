#!/use/bin/env python

# Import the world
import sys

# Initialization
consonent = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

vowel = ['a','e','i','o','u']

c1 = 0
c2 = 0
c3 = 0
v1 = 0
v2 = 0
v3 = 0

# Loop through possibilities starting with consonents
for c1 in consonent:
	for v1 in vowel:
		for c2 in consonent:
			for v2 in vowel:
				for c3 in consonent:
					for v3 in vowel:
						print c1 + v1 + c2 + v2 + c3 + v3


