# Article Summarizer

A Python tool that summarizes articles two different ways: a frequency based extractive algorithm I built from scratch, and a real LLM (via Groq's free API) for comparison. Point it at a folder of articles, pick a method, and it saves a summary file for each one.

## How it works

**Extractive method:**
1. Read each article from a `.txt` file
2. Split it into sentences
3. Count word frequency across the article, ignoring stopwords ("the", "a", "and", etc.)
4. Score each sentence by the *average* frequency of its words (not the sum - see "Bugs I ran into" below for why that matters)
5. Pick the top N highest scoring sentences, put them back in their original order, and join them into a paragraph
6. The extractive method also reports a compression stat (e.g. "280 words -> 51 words")

**AI method:**
Sends the full article to an LLM (currently `openai/gpt-oss-20b`, hosted free on Groq) with a prompt asking for an N sentence summary. This is *abstractive* - it generates new sentences rather than lifting them directly from the article.

## Usage
1. Clone the repo and install dependencies:
   ```
   pip install groq python-dotenv
   ```
2. Get a free API key from [console.groq.com](https://console.groq.com) and create a `.env` file in the project folder:
   ```
   GROQ_API_KEY=your_key_here
   ```
3. Drop `.txt` articles into the `articles/` folder
4. Run it:
   ```
   python summarizer.py
   ```
5. Choose a method (extractive, AI, both) and how many sentences you want
6. Check the `summaries/` folder - each article gets its own output file(s), named like `bees_extractive.txt` and `bees_ai.txt`

## Project structure

```
article-summarizer/
├── summarizer.py
├── .env              (not tracked - holds your API key)
├── .gitignore
├── articles/          (input articles go here)       
├── summaries/         (generated output, not tracked)
└── README.md
```

## Bugs I ran into (and what I learned from them)

This project started as a Python refresher after some time away from coding, so almost every bug here taught me something concrete:

- **Length bias in scoring**: summing word frequencies per sentence unfairly favored long sentences. Switched to an *average* score per word instead.
- **Punctuation fragmenting word counts**: `"python"` and `"python."` were counted as separate words until I stripped punctuation before counting.
- **Paragraph breaks silently merging sentences**: splitting on `". "` missed boundaries across paragraph breaks (`".\n\n"`), so I normalized newlines to spaces first.
- **File encoding corrupting special characters**: reading without `encoding="utf-8"` mangled em-dashes in the source text.
- **Stopword filtering changed which sentences got picked**, not just the word frequency dictionary; short, content-dense sentences could finally compete fairly against longer ones padded with filler words.
- **Accidentally exposed an API key once** by pasting terminal output that included it. Revoked it immediately and regenerated; a good reminder that `.gitignore` -ing `.env` protects against *committing* a key, but not against pasting it somewhere by accident.
- **No input validation on user prompts**: bad input (letters instead of numbers, out of range menu choices, zero/negative sentence counts) used to crash the program. Added validation loops that catch these and re-prompt instead, plus a warning when the requested sentence count exceeds what an article actually has.

## Extractive vs. AI: what I actually noticed

Running both on the same article side by side, the difference is obvious: my extractive version pulls real sentences verbatim, so it's faithful to the original wording but can read a little disjointed since the sentences weren't written to flow into each other. The AI version paraphrases and adds transitions, so it reads more smoothly, but it's no longer the article's exact words. Neither is strictly better - they're genuinely different tools depending on whether you need exact original phrasing or just the gist of it.

## Ideas for later

- Let the user pick the AI model instead of hardcoding one
- A simple web interface instead of command-line prompts

## Built with

Python standard library (`string`,`os`,`textwrap`) plus `groq` and `python-dotenv` for the AI summary feature.