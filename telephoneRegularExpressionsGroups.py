import re

phoneNumberRegex = re.compile(r'(\d\d\d\d\d)-(\d\d\d\d\d\d)') #separate with parenthis
matchObject = phoneNumberRegex.search("my telephone number is 01482-875668")
print(matchObject.group()) #whole search
print(matchObject.group(1)) #first part of number
print(matchObject.group(2)) # second part of number

print()

ironRegex = re.compile(r'(iron|ant)man') #pattern i want it to match either ironman or antman
mo = ironRegex.search("I love ironman 3000")
print(mo.group())
mo = ironRegex.search("antman is well funny")
print(mo.group())

#phone number with optional area code
# ? zero or one time
# * zero or more times
# + one or more
# place a back slash before to litrally find special characters /*
phoneNumberRegex = re.compile(r'(\d\d\d\d\d)?\d\d\d\d\d\d') #separate with parenthis
matchObject = phoneNumberRegex.search("my telephone number is 01482-875668")
print(matchObject.group())
print("still matching without areas code")
matchObject = phoneNumberRegex.search("my telephone number is 875668")
print(matchObject.group())


                        
