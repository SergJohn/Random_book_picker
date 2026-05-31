# Book Club

A simple Streamlit app that randomly picks a book from a list — perfect for when your book club can't agree on what to read next.

## How it works

Upload a CSV file with your book list, and the app will randomly select one title after a short suspenseful countdown.

## Getting started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app_book.py
```

### 3. Upload your book list

The app accepts a `.csv` file where each line is a book entry. A sample list is included in `books_sample.csv`:

```
The Midnight Library - Matt Haig
Dune - Frank Herbert
1984 - George Orwell
...
```

## Project structure

```
Book_club/
├── app_book.py       # Main Streamlit app
├── books_sample.csv         # Sample list of 30 books with authors
└── requirements.txt  # Python dependencies
```

## Requirements

- Python 3.8+
- Streamlit
