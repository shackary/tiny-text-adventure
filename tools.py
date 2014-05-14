#Makes a list out of a line-delimited text file
def build_list(filename):
	list = []
	contents = open(filename)
	line = contents.readline()
	while line:
		line.strip()
		list.append(line)
		line = contents.readline()
	for e in range (0, len(list) - 1):
		list[e] = list[e][:-1]
	contents.close()
	return list

#Builds a dictionary from a text file in the format key:value\n
def build_dictionary(filename):
	dictionary = {}
	contents = open(filename)
	line = contents.readline()
	while line:
		point = line.find(':')
		dictionary[line[:point]] = line[point + 1: -1]
		#go to the next line of the doc
		line = contents.readline()
	contents.close()
	return dictionary

#Pulls a block of text from a file starting with textid enclosed in {}
def pull_text(filename, textid):
	contents = open(filename).read()
	pullstart = contents.find("{", contents.find(textid)) + 1
	pullend = contents.find("}", pullstart)
	return contents[pullstart:pullend]	
	
#Pauses for a player response.
def pause(punctuation = "\npress ENTER...\n"):
	return raw_input(punctuation)

#Gives user a hard time if they don't answer a yes/no question
def ynbull(action, yeslist, nolist):
	actionbull = 0
	while action not in yeslist and action not in nolist:
		print "Try again.  This isn't a difficult question"
		action = pause("y/n: ")
		actionbull +=1
		if actionbull == 10:
			print "\nFine.  Come back when you're ready.  And don't lie next time."
			break
	
#Give a "Press ENTER to quit." prompt
def endgame():
	pause("\nPress ENTER to exit.")
	
