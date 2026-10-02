# Article Summarizer

A simple extractive text summarizer written in Python. Give it an article, and it picks out the most important sentences to generate a short summary - no external APIs or machine learning models, just frequency based scoring built from scratch.

## How it works

1. **Read the article** from a `.txt` file
2. **Split it into sentences** (on `". "`, after normalizing paragraph breaks)
3. **Count word frequency** across the whole article, ignoring common stopwords ("the", "a", "and" etc.) so the scoring reflects meaningful content rather than filler
4. **Score each sentence** by the average frequency of its words - this rewards sentences that are dense with important terms, rather than just long sentences that repeat common words
5. **Return the top-N highest scoring sentences**, in their original order, as the summary

## Example

```
$ python summarizer.py

Dreams can contain elements from everyday life
During REM sleep, brain activity becomes more similar to waking activity, and vivid dreams are particularly common
Interestingly, people do not always remember their dreams
```

## Usage

1. Save the article you want to summarize as `myarticle.txt` in the same folder as `summarizer.py`
2. Run the script:
   ```
   python summarizer.py
   ```
3. The top 3 sentences print to the terminal as the summary

## What I learned building this

This was a hands-on refresher project after some time away from coding, so a few things stood out while building it:

- **Length bias in naive scoring**: summing word frequencies per sentence unfairly favors longer sentences. Switching to an *average* score per word fixed this.
- **Punctuation fragmenting word counts**:`"python"` and `"python."` were initially counted as different words until stripping punctuation before counting.
- **Paragraph breaks merging sentences**: splitting on `". "` alone missed sentence boundaries across paragraph breaks (`".\n\n"`), which required normalizing newlines first.
- **File encoding matters**: reading a `.txt` file without specifying `encoding="utf-8"` corrupted special characters like em-dashes in the source text.
- **Stopwords meaningfully change results**: filtering out filler words didn't just clean up the word frequency dictionary - it changed which sentences actually ranked highest, since short, content dense sentences could now compete fairly against longer ones padded with common words.

## Possible next steps

- Let the user choose the number of summary sentences
- Accept pasted input directly, not just `.txt` files
- Compare against an AI-generated summary (via an LLM API) as a stretch goal
- Handle sentence splitting edge cases like abbreviations ("U.S.", "e.g.") more robustly

## Tech

Pure Python standard library only (`string`, no third-party dependencies for the core version).