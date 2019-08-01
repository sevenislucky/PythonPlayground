import re
beginsWithHelloRegex = re.compile(r'^Hello')
#use of the ^ at the begining will register a match only if its the first word
# within the string
print(beginsWithHelloRegex.search('Hello there!'))

#this will return None
print(beginsWithHelloRegex.search('He said Hello'))

# using $ at the end of a word will only match if its at the end of the string
endsWithHelloRegex = re.compile(r'War$')
print(endsWithHelloRegex.search('Avengers Infinity War'))

# this will return None
print(endsWithHelloRegex.search("War of the worlds"))

#using the ^ along with $ and \d+ (one or more digits
#will match if string is numerical from begining to end

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('01482875668'))

#this will return none due to the space
print(allDigitsRegex.search('01482 875668'))

#find any word that contains the 'ate' in the string
atRegex = re.compile(r'.ate')
print(atRegex.findall("bate fate cate pate late gate slate "))

# update to include extra string to capture the whole word "slate"
atRegex = re.compile(r'.{1,2}ate')
print(atRegex.findall("bate fate cate pate late gate slate "))

# print only the fist name and last name of a particular string
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Kev Last Name: Wilko'))

mySong = '<What do you get when you fall in love?> a massive CSA bill!>'

# only goes to the first >
nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall(mySong))

# print all
greedy = re.compile(r'<(.*)>')
print(greedy.findall(mySong))

ThreeLawsOfRobotics = ' 1. A robot may not injure a human being,or, through inaction, allow another human being come ot harm.\n 2. A robot must obey the orders giben to itby human beings except  where such orders would conflict with the first law.\n 3. A robot must protect its own existence as long as such protection does not conflict with the first and second law.'

print(ThreeLawsOfRobotics)

findeverything = re.compile(r'.*', re.DOTALL)
print(findeverything.search(ThreeLawsOfRobotics))


