def isATelephoneNumber(text):
    if len(text) != 12:
        return False # not a telephone number
    
    for i in range(0,5):
        if not text[i].isdecimal():
            return False # not a telephone number (no area code)
        
    if text[5] != "-" and text[5] != " ":
        return False # not a telephone number (missing space or dash)
     
    for i in range(6, 12):
        if not text[i].isdecimal():
            return False # not a telphone number (last six digits are worng)

    return True

print (isATelephoneNumber("01553 772741"))
print (isATelephoneNumber("01553-772741"))
print (isATelephoneNumber("01553772741"))
print (isATelephoneNumber("0153 8772741"))

print("")

print("Finding number within strings")
print("Call me 01553 772741, or at 01903-875668")
message = "Call me 01553 772741, or at 01903-875668"
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isATelephoneNumber(chunk):
        print("phone number found: " + chunk)
        foundNumber = True

if not foundNumber:
    print("Could not find any numbers.")

