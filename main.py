import csv
import re
total_words = 0
total_letters_and_digits = 0
total_sentences = 0
with open("text.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        for cell in row:


            words = cell.split()
            total_words += len(words)
            longest_word = ""
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word



            sentences = re.split(r"[.!?]", cell)
            count = 0
            for s in sentences:
                if s.strip():
                    count+= 1
            total_sentences += count


            avg = total_words / total_sentences

            for letter_digit in cell:
                if letter_digit.isalpha() or letter_digit.isdigit():
                    total_letters_and_digits += 1




print(f"The amount of total words is: {total_words}")
print(f"The amount of total letters and digits is: {total_letters_and_digits}")
print(f"The amount of total sentences is: {total_sentences}")
print(f"The average words per sentence is: {int(avg)}") if avg.is_integer() else print(f"The average words "
                                                                                  f"per sentence is: {avg:.2f}")
print(f"The longest word is: {longest_word}")






