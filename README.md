# Text-Analyzer
A simple Python script that analyzes text data stored in a CSV file.
## Features
This program reads a `text.csv` file and calculates:

- Total number of words
- Total number of sentences
- Total number of letters and digits
- Average words per sentence
- Longest word in the CSV file

## How it works
The script processes each cell in the CSV file and:
- Splits text into words
- Detects sentences using punctuation (`. ! ?`)
- Counts alphanumeric characters
- Tracks the longest word found
