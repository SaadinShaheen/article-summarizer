import string
import textwrap #textwrap is used to format and wrap text mainly by controlling how long each line can be
         # textwrap.fill() breaks the text into lines and returns it as one string, The width parameter specifies the maximum line length

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
     #replaces newline characters with spaces

    sentences=cleaned.split(". ") 
     #splits the article into sentences based on period followed by a space (not a perfect solution, but works for this example)
    
    words=cleaned.lower().split() 
     #splits the article into words based on spaces and converts them into lowercase

    freq={}
    for w in words:
        w = w.strip(string.punctuation) 
         #removes punctuation from the beginning and end of each word
        if w not in stopwords: #to filter filler words
            if w in freq:
                freq[w]+=1
            else:
                freq[w]=1

    sentence_scores=[]
    for index, s in enumerate(sentences): #enumerate is used to loop through items while keeping track of thier position/number
        words_in_sentence = s.lower().split()
        score=0
        for w in words_in_sentence: 
            w = w.strip(string.punctuation)
            score += freq.get(w, 0) 
             #adds the frequency of each word in the sentence to the score
        if len(words_in_sentence)>0:
            avg_score = score / len(words_in_sentence) 
             #calculates the avg score for the sentence by dividing the score by the length of words in the sentence
        else:
            avg_score = 0
        sentence_scores.append((index, s, avg_score))

    sorted_by_score = sorted(sentence_scores, key=lambda x:x[2], reverse = True) 
     #sorts the sentences based on their avg score in the descending order

     # lambda is used to create a small, one line function without a name
    
    top_n = sorted_by_score[:n] 
     #gets the top n sentences with highest avg score
    
    top_n_in_order = sorted(top_n, key=lambda x:x[0])
    summary_para = " ".join(add_period(s) for index, s, score in top_n_in_order)
    
    # Compression stats
    summary_word_count = len(summary_para.split())
    return summary_para, len(words), summary_word_count

# TEST
test_text = "The sky is blue. The grass is green. Water is wet and clear. Dogs are loyal animals. Cats are independent creatures."
summary, original_count, summary_count = summarize(test_text, 2)
print(summary)
print(f"{original_count} words -> {summary_count} words")