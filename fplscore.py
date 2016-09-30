#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import operator

teams = {'rounaq' : {'Harry  Kane', 'Anthony  Martial', 'Jermain  Defoe', 'Abel  Hernández', 'Enner  Valencia', 'Marouane  Fellaini', 'Marcus  Rashford', 'Wes  Morgan', 'Gary  Cahill', 'Robert  Huth'},
'adi': {'Roberto  Firmino', 'Manuel  Nolito', 'Divock  Origi', 'Islam  Slimani', 'Georginio  Wijnaldum', 'Winston  Reid', 'Shane  Long', 'Dejan  Lovren', 'Kelechi  Iheanacho', 'Patrick  van Aanholt'},
'aahir': {'Alexis  Sánchez', 'David  Silva', 'Paul  Pogba', 'Toby  Alderweireld', 'Alex  Chamberlain', 'Eric  Bailly', 'Christian  Christian Benteke', 'Kelechi  Iheanacho', 'Theo  Walcott', 'Joel  Matip'},
'hrishi': {'Sergio  Agüero', 'Sadio  Mané', 'Bamidele  Alli', 'David  David Luiz', 'Yannick  Bolasie', 'Salomón  Rondón', 'David  de Gea', 'Leighton  Baines', 'Gastón  Ramírez', 'Yannick  Bolasie'},
'varun': {'Mesut  Özil', 'Vincent  Janssen', 'Daniel  Sturridge', 'Andre  Gray', 'César  Azpilicueta', 'Simone  Zaza', 'Nacho  Monreal', 'Lucas  Pérez', 'Raheem  Sterling', 'Nicolás  Otamendi'},
'kishen': {'Álvaro  Negredo', 'Diego  Costa', 'Marko  Arnautovic', 'Gylfi  Sigurdsson', 'Yohan  Cabaye', 'Christian  Fuchs', 'Aleksandar  Kolarov', 'Santiago  Cazorla', 'Troy  Deeney', 'Neil  Taylor'},
'zubin': {'Zlatan  Ibrahimovic', 'Dimitri  Payet', 'Michy  Batshuayi', 'Fernando  Llorente', 'Cristhian  Stuani', 'Hal  Robson-Kanu', 'Laurent  Koscielny', 'Pedro  Pedro', 'Kurt  Zouma', 'Nathaniel  Clyne'},
'merv': {'Christian  Eriksen', 'Philippe  Coutinho', 'Héctor  Bellerín', 'Kevin  Mirallas', 'Xherdan  Shaqiri', 'Daley  Blind', 'Thibaut  Courtois', 'Willian  Willian', 'Leroy  Fer', 'Michail  Antonio'},
'amrit': {'Olivier  Giroud', 'Riyad  Mahrez', 'Charlie  Austin', 'Dusan  Tadic', 'Jack  Wilshere', 'Borja  Bastón', 'Kyle  Walker', 'John  Stones', 'Wilfried  Bony', 'Marcos  Alonso'},
'nava': {'Kevin  De Bruyne', 'Jamie  Vardy', 'Nathan  Redmond', 'Erik  Lamela', 'Robert  Snodgrass', 'Andros  Townsend', 'Antonio  Valencia', 'Branislav  Ivanovic', 'Bacary  Sagna', 'Etienne  Capoue'},
'korodo': {'Romelu  Lukaku', 'Henrikh  Mkhitaryan', 'André  Ayew', 'Wayne  Rooney', 'Sofiane  Boufal', 'Luke  Shaw', 'Leroy  Sané', 'Shkodran  Mustafi', 'Adnan  Januzaj', 'Jonny  Evans'},
'arkay': {'Eden  Hazard', 'Odion  Ighalo', 'Cesc  Fàbregas', 'Ahmed  Musa', 'Danny  Rose', 'Seamus  Coleman', 'Callum  Callum Wilson', 'Petr  Cech', 'Loïc  Remy', 'Oscar  Oscar'}}

fpl_data = open('fpldata.txt').read()

data = json.loads(fpl_data)
final_scores = {}
total_score = 0
for buddy in teams:
	print(buddy) 
	for player in teams[buddy]:
		player = player.split("  ")
		if len(player) != 2:
			print("Error: " + str(player))
		first_name = player[0]
		web_name = player[1]
		for i in data['elements']:
			if i['web_name'] == web_name and i['first_name'] == first_name:
					print(str(i['first_name']) + " " + str(i['web_name']) + " : " + str(i['event_points']))
					total_score = total_score + i['event_points']
		web_name = ''
		first_name = ''
	print("Total : " + str(total_score) + "\n")
	final_scores[buddy] = total_score
	total_score = 0

sorted_final = sorted(final_scores.items(), key = operator.itemgetter(1), reverse = True)
print(sorted_final)
ftable = open('table.txt', 'a')
ftable.write("Gameweek 3: " + str(sorted_final))
 

