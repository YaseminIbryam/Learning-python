import re

# Regex Methods:

# findall() - Returns a list containing all matches
text = "The rain in Spain"
matches = re.findall("ai", text)
print(matches)  # Prints: ['ai', 'ai']

# search() - Searches the string for a match and returns a Match object if there is a match
text = "The rain in Spain"
match = re.search("\s", text)
print(match)  # Prints: <re.Match object; span=(3, 4), match=' '>

# split() - Splits the string at each match and returns a list
text = "The rain in Spain"
matches = re.split("\s", text)
print(matches)  # Prints: ['The', 'rain', 'in', 'Spain']

# sub() - Replaces one or many matches with a string
text = "The rain in Spain"
new_text = re.sub("\s", "-", text)
print(new_text)  # Prints: The-rain-in-Spain

# finditer() - Returns an iterator yielding Match objects over all non-overlapping matches
text = "The rain in Spain"
matches = re.finditer("\s", text)
for match in matches:
    print(match.span())  # Prints: (3, 4)

# match() - Determine if the regex matches at the beginning of the string
text = "The rain in Spain"
match = re.match("^The", text)
print(match)  # Prints: <re.Match object; span=(0, 3), match='The'>

# fullmatch() - Determine if the regex matches the entire string
text = "The rain in Spain"
match = re.fullmatch("The rain in Spain", text)
print(match)  # Prints: <re.Match object; span=(0, 17), match='The rain in Spain'>
