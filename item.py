#! /usr/bin/python3
# -*- coding: utf-8 -*-

#= TODO ========================================================================

# oggetti da inserire sotto forma di lista di tuple
# [( '', '', '', ''), ('', '', ... ]
# la tupla è immutaile e va creata già finita
#Oggetto = collections.namedtuple('Oggetto',['classe', 'livello', 'rarita', 'prefisso', 'tipo', 'suffisso'])
# lista=[]
# lista.append(Oggetto('wizard', '12', 'common', 'inestimabile', 'light', 'babies'))
# commento inserito solo per fare prove con git

#= IMPORT ======================================================================

import sys
import collections
import re

#= COSTANTI ====================================================================


eq_necromancer 	= ['Boots', 'Ring', 'Wand', 'Staff', 'Necklace', 'Wizard Hat', 'Cloak', 'Robes']
eq_ninja 	= ['Boots', 'Robes', 'Nunchaku', 'Star', 'Belt', 'Dagger']
eq_druid	= ['Robes', 'Staff', 'Belt', 'Candle', 'Mushroom', 'Light', 'Lantern', 'Torch', 'Ring']

eq_all = { 'necromancer': eq_necromancer,
		'ninja': eq_ninja,
		'druid': eq_druid }

eq_type = eq_druid + eq_necromancer + eq_ninja

prefix = set()
suffixes = set()
rarities = set()
#equip = set()

postfix = {}
global_results = []

line_num = 0
pg_class = ''

#cerca_cifra = re.search('[0-9]{1,2}', s1)
#tr = re.search('(?P<rarities>\w+) (?P<numero>[0-9]{1,2})', s1)

#= MAIN ========================================================================

item = collections.namedtuple('item',['classe', 'livello', 'rarita', 'prefisso', 'tipo', 'suffisso'])

if len(sys.argv)>1:
	file_name = sys.argv[1]
else:
	print("no file specified!")
	sys.exit()

inputfile = open(file_name)

for line in inputfile:
	line_num +=1
		
	#= Rarita' ==========
	if not re.search('^$', line) and not re.search('^OCR', line):

		#= CLASS =========
		label_class = re.search('^#[Cc]lass[ ]{1,}(?P<class>\w+)', line)
		#print(label_class.group('class'))
		if label_class: 
			pg_class = label_class.group('class')
			print(pg_class)
		else:
			#= PREFIX =========
			for type in eq_type:
				riga = re.search(type,line)
				if riga: break
			if riga:
				pref = 'None'
				end_prefix = riga.span()[0]
				if end_prefix != 0:
					pref=line[:end_prefix -1]
					#print(pref)
					prefix.add(pref)		
	
			else:
				print ("tipo eq problematico (forse non nella lista?) a riga  ", line_num, ": ", line)
				
			#= RARITY & LEVEL =====
			tr = re.search('.{1,}of[ ]{1,}(?P<suffix>.{1,})[ ]{1,}(?P<rarities>\w+)[ ]{1,}(?P<level>[0-9]{1,2})', line)
			if tr:
				level =(tr.group('level'))

				rarity=(tr.group('rarities'))
				rarities.add(rarity)
				
				suffix = tr.group('suffix')
				suffixes.add(suffix)
			else:
				tr = re.search('[ ]{1,}(?P<rarities>\w+)[ ]{1,}(?P<level>[0-9]{1,2})', line)
				if tr:
					rarities.add(tr.group('rarities'))
					suffix = 'None'
					
			print(line_num,': ', pg_class, rarity, pref, type,'of' ,suffix, level)
			global_results.append(item(pg_class, level, rarity, pref, type, suffix))
			#item = collections.namedtuple('item',['classe', 'livello', 'rarita', 'prefisso', 'tipo', 'suffisso'])
		
#= PRINT ==========
print("PREFIX")
s_prefix = sorted(prefix)
for p in s_prefix:
	print(p, end=", ")

print("\n====================")
print (sorted(rarities))
print("====================")
#print (equip)
print (suffixes)
