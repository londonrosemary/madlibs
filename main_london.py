madlib = "DING DING DING! The bell sound make all the children {VERB} to the {NOUN}. It's recess time! The time of day when {ADJECTIVE} kids can forget their {PLURALNOUN} and have some fun!"

print("Verb:")
VERB = input()
print("Noun:")
NOUN = input()
print("Adjective:")
ADJECTIVE = input()
print("Plural Noun:")
PLURALNOUN = input()

madlib = madlib.replace("{VERB}", VERB)
madlib = madlib.replace("{NOUN}", NOUN)
madlib = madlib.replace("{ADJECTIVE}", ADJECTIVE)
madlib = madlib.replace("{PLURALNOUN}", PLURALNOUN)

print(madlib)
