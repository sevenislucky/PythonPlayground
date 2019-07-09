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


newPhoneNumberRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
webpageinfo = """


 
HOME
AREA CODES
MOBILE PHONES

Who Called Me ?
Phone number checker
 

Our completely free lookup has saved visitors tens of millions of pounds!


Know who called with Free reverse phone lookup!
Did you receive a call from an unknown number?
Not sure if you should receive?
Are you tired of offers banks, debt collectors or ordinary scammers?
who-called.co.uk - offers the reverse phone number lookup tool! The largest and most trusted online telephone number database. If you want to find out more about who called you, start a phone number search by entering the number above. Identify telephone and cell phone numbers, all types of phone calls including spam and scam calls and simply know more about who called. Trusted by over 10 million people every month helping visitors in over 250 million free reverse searches! 

LET'S BE FRIENDS!




Latest telephone numbers reported

PHONE NUMBER
COMMENT

01234343365 
HMRC scammer...
a few seconds ago 


01513653280 
They have tried calling me numerous...
a few seconds ago 


01242026645 
Unknown number...
a few seconds ago 


67215923347 
Rang three times and cut off. Registered...
a few seconds ago 


07596301478 
Victoria Limiting - motor accident...
a few seconds ago 

What are scams using missed calls and text messages from unknown numbers?
Missed call scams start by ringing your phone and hanging up so quickly that you can’t answer the call in time. Your phone registers a missed call and you probably won’t recognise the number. People will often then call the number back to find out who it is. Apart from being a nuisance, the missed call can lead to a scam in two ways
The number you call back may be redirected to a premium rate service (a number that starts with 09) without your knowledge, which means you will be charged a lot of money per minute.

The number may tell you that you have won a prize of some sort and give you another number to call to ‘claim’ your prize, but they may not tell you how much the call will cost. This second number may be a premium rate number, again charging you a lot of money to get your prize.
Text message scams work by sending you a text message from a number you may not recognise, but the content of the message could sound like it’s from a friend—for instance "Hi, it’s John. I’m back! When do you want to catch up?" or "Hey big fella, happy birthday!". Another common tactic is for a text message to sound like someone flirting with you. Many people reply asking who it is and end up engaging in a lengthy SMS exchange with the scammer. Only later do they find out that they have been charged a high rate both for messages they sent (sometimes there are also charges for messages received as well).

Warning signs
You receive a ‘missed call’ from a number that you don’t recognise.
You didn’t hear your phone ring.
The number starts with 09 (which is a premium rate service)
You receive a text from a number you don’t recognise, but which sounds like it’s from a friend.
If you return a missed call, a recorded message asks you to dial a different number (often starting with 09) but the cost of the call is not clearly stated.
Protect yourself from scams using missed calls and text messages from unknown numbers
It is best not to respond to text messages or missed calls that come from numbers you don’t recognise.
Be careful of phone numbers beginning with 09. These are charged at a premium rate and can be very expensive.
Look out for SMS and MMS numbers that start with 09. These are charged at a premium rate (sometimes even for receiving a message) and can be very expensive.
Report them
If you have received such a call or text, or if you have returned the call or text and you now realize it is a scam, you can report it on our website. You should also spread the word to your friends and family to protect them.
Geographic numbers
01 and 02 numbers These numbers are related to specific locations in the UK and are used for homes and businesses. Calls from landlines are typically charged up to 9p per minute; calls from mobiles between 3p and 40p per minute depending on your call package. For landlines there is normally also a call set-up fee, and call charges are dependent on the time of day. Most providers offer call packages that allow calls free of charge at certain times of the day.
Premium rate number guide
Short text message numbers Mobile text short code numbers are five or six-digits long and usually begin with 5, 6, 7 or 8. These numbers are often used to pay for new features in apps, to donate to charity, to enter competitions and to download games and ringtones. You may see these numbers in promotions asking you to text a certain word to a number or, you may receive promotional texts asking you to reply to them.
118 – directory enquiries Numbers beginning with 118 are used for directory enquiries services.Costs: Most calls include a charge to connect (can be between 50p and £4) and then a charge for every minute you use the line (can be up to £5 per minute).
0871, 0872 or 0873 These numbers are normally used for customer service lines, such as technical support lines, chat lines, tarot/horoscope lines and sales/booking lines. Costs: Typically, between 11p and 15p per minute from a BT landline and between 20p and 41p per minute from mobiles. The cost of calling 087 numbers is made up of two parts: an access charge going to your phone company, and a service charge set by the organisation you are calling.
070 numbers Numbers beginning with 070 may look like mobile numbers but they are different and can be more expensive.They are used to divert calls to another phone number. Small businesses and sole traders often used these to avoid giving out their personal phone number.070 numbers are regulated by Ofcom. However, PhonepayPlus can investigate services on these numbers if they are found to offer premium rate-style services and/or the number is being misused and if the cost of the call exceeds 10p per minute.
09 numbers These numbers are mainly used for competitions, TV voting, horoscopes, chat lines, adult lines and professional service lines.Costs: Between 9p and £1.69 per minute from a BT landline (other landlines up to £2.60 per minute) or between 50p and £2.50 per minute from mobiles
Contact the company that runs the service
If you want to make an enquiry about your charge, you should first contact the company that is running the service.
To find out who is running the service and the contact details of the company, please use our search engine or contact your telephone provider and ask for the contact details of the service provider.
What is an SMS competition & trivia scam?
An SMS competition or SMS trivia scam usually arrives as a text message and may encourage you to enter a competition for a great prize (like an mp3 player). The message (or sometimes, an advertisement) could also invite you to take part in a trivia competition, with a great prize on offer if you answer a certain number of questions correctly. The scammers make money by charging extremely high rates for the messages you send, and any further messages they send to you. These charges could be as high as £2 for each message sent and/or received. With trivia scams, the first lot of questions will be very easy. This is meant to encourage you to keep playing. However, the last one or two questions that you need to answer to claim your ‘prize’ could be very difficult or impossible to answer correctly (and may even require you to guess a random number).
Warning signs
You receive a text message offering you the chance to win a great prize by sending a return text to enter a competition.
A text message tells you that you could win a great prize by participating in a trivia competition over SMS. The first message may even contain a very easy question to tempt you.
The text message (or other advertisement) does not give you details about how to stop receiving more messages
The first text message, or the advertisement for the competition does not contain all the terms and conditions.
Protect yourself from SMS competition & trivia scams
Use your common sense: the offer may be a scam.
Read all the terms and conditions of any offer very carefully: claims of free or very cheap offers often have hidden costs.
Make sure you know how to stop any subscription service you want to sign up to.
It is best not to respond to text messages or missed calls that come from numbers you don’t recognise.
Be careful of phone numbers beginning with 09. These are charged at a premium rate and can be very expensive
Look out for SMS and MMS numbers that start with 09. These are charged at a premium rate (sometimes even for receiving a message) and can be very expensive.

DANGEROUS NUMBERS
01234343365 
HMRC scammer...
01287577139 
Recorded message...
03002009124 
This is similar...
02085234968 
Already blocked...
01242022864 
Silent call....
08005453013 
09/July/2019....
07583620017 
Just called...
01242027496 
Scam. Recorded...
60645 
Scam I was...
08443570723 
08443570723...
© who-called.co.uk. All rights reserved. Google+ 
HOME PRIVACY POLICY TERMS OF SERVICE CONTACT 

This site uses cookies, including of third parties, to send you advertisements and services in line with your preferences.Please be advised that by continuing to use this Website, without changing your browser settings, you consent to the use of cookies.Got it!
"""
print(newPhoneNumberRegex.findall(webpageinfo))

# \d any digit
# \D any letter
# \s spaces
# \w words

