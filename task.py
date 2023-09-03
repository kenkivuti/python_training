# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
# name = “  JOHn  .“ to “john”

name = "  JOHn  ."

print(name.strip().replace("  ","").lower())

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”

sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

