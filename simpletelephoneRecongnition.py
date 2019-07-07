import re # regular expression module


message = "Call me 01553 772741, or at 01903-875668"

phoneNumRegexpression = re.compile(r"\d\d\d\d\d-\d\d\d\d\d\d")
mo = phoneNumRegexpression.search(message)
print(mo.group())
