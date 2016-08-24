#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import operator

teams = {'rounaq' : {'Harry  Kane', 'Anthony  Martial', 'Jermain  Defoe', 'Abel  Hernández', 'Enner  Valencia', 'Chris  Smalling', 'Marcus  Rashford', 'Wes  Morgan', 'Gary  Cahill', 'Robert  Huth'},
'adi': {'Roberto  Firmino', 'Manuel  Nolito', 'Divock  Origi', 'Andy  Carroll', 'Georginio  Wijnaldum', 'Winston  Reid', 'Shane  Long', 'Alberto  Moreno', 'Kelechi  Iheanacho', 'Patrick  van Aanholt'},
'aahir': {'Alexis  Sánchez', 'David  Silva', 'Paul  Pogba', 'Toby  Alderweireld', 'Alex  Iwobi', 'Eric  Bailly', 'Christian  Benteke', 'Juan  Cuadrado', 'Theo  Walcott', 'Joel  Matip'},
'hrishi': {'Sergio  Agüero', 'Sadio  Mané', 'Bamidele  Alli', 'Jesse  Lingard', 'Ross  Barkley', 'Salomón  Rondón', 'David  de Gea', 'Leighton  Baines', 'Oumar  Niasse', 'Jose  Fonte'},
'varun': {'Jamie  Vardy', 'Vincent  Janssen', 'Daniel  Sturridge', 'Andre  Gray', 'César  Azpilicueta', 'Joe  Hart', 'Nacho  Monreal', 'Sofiane  Feghouli', 'Raheem  Sterling', 'Connor  Wickham'},
'kishen': {'Álvaro  Negredo', 'Diego  Costa', 'Marko  Arnautovic', 'Gylfi  Sigurdsson', 'Yohan  Cabaye', 'Christian  Fuchs', 'Aleksandar  Kolarov', 'Santiago  Cazorla', 'Troy  Deeney', 'Neil  Taylor'},
'zubin': {'Zlatan  Ibrahimovic', 'Dmitri  Payet', 'Michy  Batshuayi', 'Fernando  Llorente', 'Danny  Ings', 'Wilfred  Zaha', 'Laurent  Koscielny', 'Pedro  Pedro', 'Kurt  Zouma', 'Nathaniel  Clyne'},
'merv': {'Christian  Eriksen', 'Philippe  Coutinho', 'Héctor  Bellerin', 'Saido  Berahino', 'Xherdan  Shaqiri', 'Aaron  Cresswell', 'Thibaut  Courtois', 'Willian  Willian', 'Benik  Afobe', 'Jefferson  Montero'},
'amrit': {'Olivier  Giroud', 'Riyad  Mahrez', 'Charlie  Austin', 'Dusan  Tadic', 'Aaron  Ramsey', 'Viktor  Fischer', 'Kyle  Walker', 'John  Stones', 'Wilfred  Bony', 'Virgil  van Dijk'},
'nava': {'Kevin  De Bruyne', 'Mesut  Özil', 'Nathan  Redmond', 'Erik  Lamela', 'Gerard  Deulofeu', 'Andros  Townsend', 'Antonio  Valencia', 'Branislav  Ivanovic', 'Bacary  Sagna', 'Jordan  Rhodes'},
'korodo': {'Romelu  Lukaku', 'Henrikh  Mkhitaryan', 'Andre  Ayew', 'Wayne  Rooney', 'Yannick  Bolasie', 'Luke  Shaw', 'Leroy  Sané', 'Hugo  Lloris', 'Adnan  Januzaj', 'Jonny  Evans'},
'arkay': {'Eden  Hazard', 'Odion  Ighalo', 'Cesc  Fabregas', 'Ahmed  Musa', 'Danny  Rose', 'Seamus  Coleman', 'Callum  Wilson', 'Petr  Cech', 'Peter  Crouch', 'Robert  Snodgrass'}}

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
					print(str(i['first_name']) + " " + str(i['web_name']) + " : " + str(i['total_points']))
					total_score = total_score + i['total_points']
		web_name = ''
		first_name = ''
	print("Total : " + str(total_score) + "\n")
	final_scores[buddy] = total_score
	total_score = 0

sorted_final = sorted(final_scores.items(), key = operator.itemgetter(1), reverse = True)
print(sorted_final)
ftable = open('table.txt', 'w')
ftable.write("\n\nGameweek 1: " + str(sorted_final))
 

