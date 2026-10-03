import string
import textwrap # textwrap is used to format and wrap text mainly by controlling how long each line can be
import os # os module lets your program interact with the operating system (like files, folders, paths and environment variables)

stopwords = {"the", "a", "an", "and", "or", 
             "but", "is", "are", "was", "were", 
             "to", "of", "in", "on","at", "for", 
             "with", "this", "that", "it", "as", 
             "by","have", "has", "do", "does"}

def add_period(s):
    s = s.strip()
    if s and s[-1] not in ".!?":
        s += "."
    return s
def summarize(article_text, n):
    cleaned=article_text.replace("\n", " ")
     # replaces newline characters with spaces

    sentences=cleaned.split(". ") 
     # splits the article into sentences based on period followed by a space (not a perfect solution, but works for this example)
    
    words=cleaned.lower().split() 
     # splits the article into words based on spaces and converts them into lowercase

    freq={}
    for w in words:
        w = w.strip(string.punctuation) 
         # removes punctuation from the beginning and end of each word
        if w not in stopwords: # to filter filler words
            if w in freq:
                freq[w]+=1
            else:
                freq[w]=1

    sentence_scores=[]
    for index, s in enumerate(sentences): # enumerate is used to loop through items while keeping track of thier position/number
        words_in_sentence = s.lower().split()
        score=0
        for w in words_in_sentence: 
            w = w.strip(string.punctuation)
            score += freq.get(w, 0) 
             # adds the frequency of each word in the sentence to the score
        if len(words_in_sentence)>0:
            avg_score = score / len(words_in_sentence) 
             # calculates the avg score for the sentence by dividing the score by the length of words in the sentence
        else:
            avg_score = 0
        sentence_scores.append((index, s, avg_score))

    sorted_by_score = sorted(sentence_scores, key=lambda x:x[2], reverse = True) 
     # sorts the sentences based on their avg score in the descending order

     # lambda is used to create a small, one line function without a name
    
    top_n = sorted_by_score[:n] 
     # gets the top n sentences with highest avg score
    
    top_n_in_order = sorted(top_n, key=lambda x:x[0])
    summary_para = " ".join(add_period(s) for index, s, score in top_n_in_order)
    
    # Compression stats
    summary_word_count = len(summary_para.split())
    return summary_para, len(words), summary_word_count

folder = "articles"
files = [f for f in os.listdir(folder) if f.endswith(".txt")] # Get all .txt files from the folder
if not files:
    print("No .txt files found in the articles folder")
n = int(input("How many sentences per summary? "))

for filename in files:
    path = os.path.join(folder, filename) # os.path.join() is used to combine folder and file names into a proper file path
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    summary, original_count, summary_count = summarize(text, n)
    compression = round((summary_count/original_count) * 100, 1)

    print(f"\n--- {filename} ---")
    print(textwrap.fill(summary, width=70)) # textwrap.fill() breaks the text into lines and returns it as one string, The width parameter specifies the maximum line length
    print("="*50)
    print(f"Original: {original_count} words | Summary: {summary_count} words | Compressed to {compression}% of original")
    print("="*50)