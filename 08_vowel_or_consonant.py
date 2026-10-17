# Vowel or Consonant

letter = input("Enter one alphabet letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter exactly one alphabet letter")
elif letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
