# Article Summarizer

A little Python script that reads an article and spits out the 3 most important sentences as a summary. No AI, no external libraries — just plain word-counting logic.

I built this mostly to get back into coding after a while away from it, so it's intentionally simple. No ML, no APIs (yet) — just Python basics applied to something that actually does a real job.

## How it works (the short version)

1. Read the article from a `.txt` file
2. Break it into sentences
3. Count how often each word shows up, ignoring boring filler words like "the," "a," "and"
4. Score each sentence based on how many "important" (frequent, non-filler) words it has
5. Print the top 3 highest-scoring sentences

That's it. It's extractive summarization — meaning it picks real sentences straight out of the article rather than generating new text like an AI model would.

## Example

```
$ python summarizer.py

Dreams can contain elements from everyday life
During REM sleep, brain activity becomes more similar to waking activity, and vivid dreams are particularly common
Interestingly, people do not always remember their dreams
```

## How to run it

1. Put the article you want summarized into a file called `myarticle.txt`, same folder as `summarizer.py`
2. Run:
   ```
   python summarizer.py
   ```
3. It prints the summary to the terminal

## Bugs I ran into (and actually learned something from)

- My first scoring method just added up word frequencies per sentence — which meant **long sentences won by default**, even if they weren't actually the most important ones. Switched to averaging the score instead, which fixed it.
- `"python"` and `"python."` were getting counted as two different words because of the trailing period. Had to strip punctuation before counting.
- Splitting sentences on `". "` quietly merged sentences across paragraph breaks, because paragraph breaks are `.\n\n`, not `. `. Fixed by replacing newlines with spaces first.
- Reading the `.txt` file without specifying UTF-8 encoding corrupted special characters (em-dashes turned into garbage symbols). Classic Windows default-encoding issue.
- Filtering out filler words didn't just clean up the word list — it actually changed which sentences got picked as "most important." That one surprised me a little.

## Ideas for later (not done yet)

- Let the user choose how many sentences they want
- Accept pasted text directly, not just `.txt` files
- Try hooking this up to an actual LLM API and compare results against my own algorithm
- Handle abbreviations ("U.S.", "e.g.") better, since right now they get mistaken for sentence endings

## Built with

Just Python's standard library (`string`). No pip installs needed.
