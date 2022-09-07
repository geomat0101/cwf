#!/bin/env python

# Matt George
# http://en.wikipedia.org/wiki/Beerware

from curses.ascii import isupper, islower
import string

f = open('words.twl')

words = set()

for word in f:
	if word[0].isupper():
		continue

	if word[-1] == "\n":
		words.add(word[:-1])
	else:
		words.add(word)

f.close()


scores = 	[
				('eaionrtlsu', 1),
				('dg', 2),
				('bcmp', 3),
				('fhvwy', 4),
				('k', 5),
				('jx', 8),
				('qz', 10),
				(' ', 0)
			]


import re
import operator

def do_search(letters, line):
	extra = ''
	for c in line:
		if c.islower():
			extra += c
	
	allowed = letters + extra

	results = set()
	pattern = re.compile(line, flags=re.IGNORECASE)

	for word in words:
		if re.search(pattern, word) is None:
			continue

		addit = True
		curr_allowed = allowed
		curr_score = 0

		display_word = word

		for c in word:
			if c not in curr_allowed:
				if ' ' in curr_allowed:
					display_word = display_word.replace(c,c.upper(),1)
					c = ' '
				else:
					addit = False
					break

			for (scorestr, score) in scores:
				if c in scorestr:
					curr_score += score
					break

			curr_allowed = curr_allowed[:curr_allowed.index(c)] + curr_allowed[curr_allowed.index(c)+1:]

		if addit:
			results.add((display_word, curr_score))
	
	return(results)


def print_results(results):
	for word, score in sorted(results, key=operator.itemgetter(1)):
		print("%5d %10s" % (score, word))
	print


def change_letters(letters):
		print("Letters set to '%s'\n" % letters)
		print("8-letter words:")
		print_results(do_search(letters + ' ', '^.{8}$'))
		print("7-letter words:")
		print_results(do_search(letters, '^.{7}$'))
		print
		return letters
	

letters = ''

while True:
	line = input('? ')
	line = line.lower()

	if line == '':
		continue

	if line[0] == '=':
		letters = change_letters(line[1:])
		continue
	
	if line[0] == '+':
		letters = change_letters(letters + ' ')
		continue
	
	if line[0] == '-':
		if ' ' in letters:
			letters = change_letters(letters[:letters.index(' ')] + letters[letters.index(' ')+1:])
		continue
	
	results = do_search(letters, line)
	print_results(results)


