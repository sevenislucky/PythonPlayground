#! python3

import re, pyperclip
#TODO: Create Regex for phone numbers
phoneRegex = re.compile(r'''
# 01553 692564, 0844 745 1111
((
((\d\d\d\d\d) | (\d\d\d\d))  #area code
(\s)   #separator
(((\d\d\d\d\d\d) | (\d\d\d)))#telephone number
(\s)   #separator
((\d\d\d\d))? # telephone
))
''', re.VERBOSE)

# if verbose mode wasnt used this is what it would have looked like!
# ((((\d\d\d\d\d) | (\d\d\d\d))(\s)(((\d\d\d\d\d\d) | (\d\d\d)))(\s)((\d\d\d\d))?))

#TODO: Create Regex for email addresses
emailRegex = re.compile(r'''
#www.+whatever@(\d{2,5}))?.com
www.+   #name
[a-zA-Z]+                # @ symbol
[a-zA-Z0-9_.]+# domain name

''', re.VERBOSE)

#TODO: Get the text off the clip board
text = pyperclip.paste()
#TODO: Extract the email/phone from the text
extracetedPhone = phoneRegex.findall(text)
#TODO: Copy the extracted email/phone to the clipboard
extracetedEmail = emailRegex.findall(text)

#print(extracetedEmail)

allTelephoneNumbers = []

for phoneNumber in extracetedPhone:
    allTelephoneNumbers.append(phoneNumber[0])

#print(allTelephoneNumbers)

results = '\n'.join(allTelephoneNumbers) + '\n' + '\n'.join(extracetedEmail)
print(results)
pyperclip.copy(results)
