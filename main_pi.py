
madlib = "Look, I guarantee there`ll be {ADJECTIVE1} times. I guarantee that at some {NOUN1}, {NUMBER1} or both of us is gonna want to get out of this {NOUN2}. But I also guarantee that if I don`t ask you to be {ADJECTIVE2}, I`ll {VERB1} it for the rest of my {NOUN3}, because I know, in my {BODYPART1}, you`re the {ADJECTIVE3} one for me."

print("Adjective:")
adjective1 = input()
print("Noun:")
noun1 = input()
print("Number:")
number1 = input()
print("Noun:")
noun2 = input()
print("Adjective:")
adjective2 = input()
print("Verb:")
verb1 = input()
print("Noun:")
noun3 = input()
print("Body part:")
bodyPart = input()
print("Adjective:")
adjective3 = input()

madlib = madlib.replace("{ADJECTIVE1}", adjective1)
madlib = madlib.replace("{NOUN1}", noun1)
madlib = madlib.replace("{NUMBER1}", number1)
madlib = madlib.replace("{NOUN2}", noun2)
madlib = madlib.replace("{ADJECTIVE2}", adjective2)
madlib = madlib.replace("{VERB1}", verb1)
madlib = madlib.replace("{NOUN3}", noun3)
madlib = madlib.replace("{BODYPART1}", bodyPart)
madlib = madlib.replace("{ADJECTIVE3}", adjective3)

print(madlib)
