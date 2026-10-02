import string
with open("myarticle.txt", "r", encoding = "utf-8") as f: 
    #Encoding tells Python how to convert bytes in a text file into readable characters.
    article = f.read() 
    #reads the entire content of the file and stores in variable article

length=len(article)
print(length)

cleaned=article.replace("\n", " ")
 #replaces newline characters with spaces ) #splits the article into sentences based on period followed by a space (not a perfect solution, but works for this example)

sentences=cleaned.split(". ") 
#splits the article into sentences based on period followed by a space (not a perfect solution, but works for this example)
print(len(sentences))

for sentence in sentences:
    print(sentence)
    print("---")

words=cleaned.lower().split() 
#splits the article into words based on spaces and converts them into lowercase

freq={}
stopwords = ["the", "a", "an", "and", "or", 
             "but", "is", "are", "was", "were", 
             "to", "of", "in", "on","at", "for", 
             "with", "this", "that", "it", "as", 
             "by","have", "has", "do", "does"]
for w in words:
    w = w.strip(string.punctuation) 
    #removes punctuation from the beginning and end of each word
    if w not in stopwords: #to filter filler words
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
print(freq)
 
sentence_scores=[]
for s in sentences:
    words_in_sentence = s.lower().split()
    score=0
    for w in words_in_sentence: 
        w = w.strip(string.punctuation)
        score += freq.get(w, 0) 
        #adds the frequency of each word in the sentence to the score
    if (len(words_in_sentence))>0:
        avg_score = score / len(words_in_sentence) 
        #calculates the avg score for the sentence by dividing the score by the length of words in the sentence
    else:
        avg_score = 0
    sentence_scores.append((s, avg_score))
sorted_sentences = sorted(sentence_scores, key=lambda x:x[1], reverse = True) 
#sorts the sentences based on their avg score in the descending order

# lambda is used to create a small, one line function without a name.

top_3 = sorted_sentences[:3] 
#gets the top 3 sentences with highest avg score
for s, score in top_3:
    print(round(score,2), "->",s)