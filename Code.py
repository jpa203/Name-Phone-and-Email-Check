import re, pyperclip 


#RegEx for Name

nameregex = re.compile(r"""

[a-zA-Z]+              # first name
\s                     # space
[a-zA-Z]+              # last name

	""",re.VERBOSE)

# RegEx for Phone Number

phoneregex = re.compile(r"""

(	

((\d\d\d)|(\(\d\d\d\)))? # area code - optional
(\s|-)                   # first separator
\d\d\d                   # first three numbers
(\s|-)                   # separator
\d\d\d\d                 # last four numbers
(((ext(\.)?\s)|x)        # extension word-part
(\d{2,5}))?              # extension number-part

)

""", re.VERBOSE)

# RegEx Email Addresses 

emailregex = re.compile(r"""

[a-zA-Z0-9_.+]+  # email name
@				 # @ symbol
[a-zA-Z0-9_.+]+  # domain name part

	""",re.VERBOSE)


# text off the clipboard

text = pyperclip.paste()

# extreact name

extract_name = nameregex.findall(text)


# extract phone number

extract_phone = phoneregex.findall(text)

# extract email address

extract_email = emailregex.findall(text)

allphonenumbers = []
for n in extract_phone:
	allphonenumbers.append(n[0])

results = '\n'.join(extract_name) + '\n' +'\n'.join(allphonenumbers) + '\n' + \
'\n'.join(extract_email)

pyperclip.copy(results)
