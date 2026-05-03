# Text-Analyzer

This Python script reads a `.csv` file and performs basic text analysis on its contents. It processes each cell in the file and calculates several statistics, including word count, sentence count, and more.

---

## Features

- Counts total number of **words**
- Counts total number of **letters and digits**
- Counts total number of **sentences**
- Calculates **average words per sentence**
- Finds the **longest word**
- Extracts and displays **email addresses**

---


## How It Works

1. Opens a file named `text.csv`
2. Reads all rows and cells using the CSV reader
3. For each cell:
   - Splits text into words
   - Counts valid characters (letters and digits)
   - Splits sentences using punctuation (`.`, `!`, `?`)
   - Searches for email addresses using regex
4. Outputs the computed statistics
