from tools import *

#These functions allow me to update what time it is.
#The only one that gets used in the game is time_change
def ampm_switch(ampm):
	if ampm == "AM":
		ampm = "PM"
	else:
		ampm = "AM"
	return ampm

def time_compute():
	global time
	amhours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
	pmhours = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
	while time > 1440:
		time -= 1440
	hour = time / 60
	if hour in amhours:
		ampm = "AM"
		if hour == 0:
			hour = 12
	else:
		ampm = "PM"
		if hour != 12:
			hour -= 12
	if time == 1440:
		ampm = "AM"
	#stuff from here on should be fine
	minutes = str(time % 60)
	if len(minutes) == 1:
		minutes = "0" + minutes
	hour = str(hour)
	return hour + ":" + minutes + ampm

def time_change(minutes):
	global game_dict
	global time
	time += minutes
	game_dict["time"] = time_compute()

#For debugging purposes, skip to different places
def skip():
	skip = raw_input("Where to skip to? ")
	if skip == "ch1":
		ch1()
	else:
		introduction()

#This gets called when the mood is decided	
def mood_parse(mood):
	global game_dict
	mood = mood.lower()
	if mood in good_mood:
		game_dict = happy_game
	elif mood in bad_mood:
		game_dict = sad_game
	else:
		game_dict = game_dict
	game_dict["name"] = name



#Allows the user to waste time if they want to
def waste_time(current_time):
	global affirmative
	global negative
	print pull_text("scenario.txt", "timewaster") % game_dict
	action = pause("y/n: ")
	ynbull(action, affirmative, negative)
	if action in negative:
		print "\tOk, nevermind then.  No hard feelings."
	else: 
		keep_going = "y"
		while keep_going in affirmative:
			timetowaste = int(pause("\nHow many minutes do you want to waste? "))
			print "\n\tOk.  It was %(time)s." % game_dict
			time_change(timetowaste)
			print "\tNow it's %(time)s." % game_dict
			keep_going = pause("\nWanna waste some more time? ")
		print "\n\tThanks.  That was fun.\n"	

#Gathers the player's name and decides if they get the sad version.
#Then it asks them if they're ready.  Trains pauses and y/n questions.
#If they're ready, starts ch1.
def introduction():
	global game_dict
	global name
	print pull_text("scenario.txt", "title")
	pause("")
	name = raw_input("\nWhat's your name?  ")
	print "\n\tThat's a nice name."
	pause()
	mood = raw_input("\nHow are you feeling today, %s?  " % name)
	mood_parse(mood) #decides what version of the text happens
	print "\n\tWell, that's just fine."
	pause()
	ready = raw_input("\nAre you ready to start, %s?  " %name)
	if ready.lower() in affirmative:
		game_dict["name"] = name
		ch1()
	else: 
		print "\n\tThen come back and see me when you are."
	
def ch1():
	global affirmative
	global game_dict
	time_change(0)
	print pull_text("scenario.txt", "room1") % game_dict
	action = pause("y/n: ")
	ynbull(action, affirmative, negative)
	if action in affirmative:
		if game_dict["version"] == "sad" or game_dict["version"] == "neutral":
			time_change(150)
			print pull_text("scenario.txt", "room1a") % game_dict
			pause()
			print pull_text("scenario.txt", "room1b") % game_dict
			pause()
			print pull_text("scenario.txt", "room2") % game_dict
		else:
			time_change(2)
			print pull_text("scenario.txt", "room2") % game_dict
	if action in negative:
		if game_dict["version"] == "happy":
			time_change(150)
			print pull_text("scenario.txt", "room1a") % game_dict
			pause()
			print pull_text("scenario.txt", "room1b") % game_dict
			pause()
			print pull_text("scenario.txt", "room2") % game_dict
		else:
			time_change(2)
			print pull_text("scenario.txt", "room2") % game_dict
	

	
	###### THIS IS WHERE THE ACTUAL ORDER OF INSTRUCTIONS GOES ######
try:
	name = ""
	time = 420
	affirmative = build_list("affirmative.txt")
	negative = build_list("negative.txt")
	good_mood = build_list("goodmood.txt")
	bad_mood = build_list("badmood.txt")
	game_dict = build_dictionary("neutral.txt")
	sad_game = build_dictionary("sadgame.txt")
	happy_game = build_dictionary("happygame.txt")
	#skip()
	introduction()
	pause()
	waste_time(time)
except: 
	print "An error has occurred.  Please try again."
	
endgame()
