import string
article = '''The application layer provides services to the user. Communication is provided using a logical
connection, which means that the two application layers assume that there is an imaginary direct
connection through which they can send and receive messages. Figure shows the idea behind this
logical connection.

Providing Services
Before the Internet, communication networks like the telephone network were designed for
specific services, such as voice communication. Over time, users adapted these networks to
provide additional services, like fax, by adding extra hardware.
The Internet, similarly designed to serve global users, is more adaptable due to the layered
structure of the TCP/IP protocol suite. Each layer in this suite can add or replace protocols, as

Computer Networks (BCS502)

Department of CSE, CEC 2
long as they work with the protocols in the layers below. This flexibility supports the evolving
nature of the Internet.
The application layer, at the top, differs because it only receives services from the transport layer
without needing to support other layers. This makes it easy to add or remove application
protocols as long as they can work with the transport layer. This flexibility allows the Internet to
continually expand with new application protocols, which has been a constant feature of its
growth since its inception.
Standard and Nonstandard Protocols
For smooth Internet operation, the protocols in the first four layers of the TCP/IP suite need to be
standardized and documented. These standard protocols are typically part of operating systems
like Windows or UNIX. However, the application-layer protocols can be both standard and
nonstandard for added flexibility.

Standard Application-Layer Protocols-Standard application-layer protocols are well-
documented and standardized by Internet authorities. They are widely used in daily Internet

interactions.
Nonstandard Application-Layer Protocols-Programmers can also create nonstandard (or
proprietary) application-layer programs by developing two programs that provide services
through the transport layer.'''
article2 = '''In the middle of busy cities, trees often go unnoticed. They stand beside roads, outside buildings, and in small parks, quietly providing benefits that are easy to overlook. Yet urban trees play an important role in making cities healthier and more comfortable places to live.

One of their most noticeable effects is temperature control. Concrete roads and buildings absorb heat during the day, causing cities to become significantly warmer than surrounding rural areas. Trees provide shade and release water vapor through a process called transpiration, helping to cool their surroundings.

Trees also improve air quality by absorbing certain pollutants and trapping dust on their leaves. Their roots help rainwater enter the soil, reducing the amount of water flowing directly into drains during heavy rainfall. In addition, trees provide habitats for birds, insects, and other small organisms, creating tiny ecosystems within otherwise highly developed areas.

Beyond their environmental benefits, trees can influence how people experience a city. Streets lined with trees can feel more pleasant for walking, while green spaces provide places for people to relax and spend time outdoors. Some studies have also associated access to urban greenery with improved psychological well-being.

However, maintaining urban trees requires careful planning. Poorly chosen species can damage sidewalks, interfere with electrical lines, or struggle to survive in polluted and compacted soil. Cities therefore need to consider factors such as native species, available space, water requirements, and long-term maintenance.

As cities continue to grow, urban trees will become increasingly important. They may appear to be simple features of the landscape, but their combined effects on temperature, air, water, wildlife, and human life make them an essential part of a sustainable city.'''

article1 = '''Welcome to Google's Python Class -- this is a free class for people with a little bit of programming experience who want to learn Python. The class includes written materials, lecture videos, and lots of code exercises to practice Python coding. These materials are used within Google to introduce Python to people who have just a little programming experience. The first exercises work on basic Python concepts like strings and lists, building up to the later exercises which are full programs dealing with text files, processes, and http connections. The class is geared for people who have a little bit of programming experience in some language, enough to know what a "variable" or "if statement" is. Beyond that, you do not need to be an expert programmer to use this material.

To get started, the Python sections are linked at the left -- Python Set Up to get Python installed on your machine, Python Introduction for an introduction to the language, and then Python Strings starts the coding material, leading to the first exercise. The end of each written section includes a link to the code exercise for that section's material. The lecture videos parallel the written materials, introducing Python, then strings, then first exercises, and so on. At Google, all this material makes up an intensive 2-day class, so the videos are organized as the day-1 and day-2 sections.

This material was created by Nick Parlante working in the engEDU group at Google. Special thanks for the help from my Google colleagues John Cox, Steve Glassman, Piotr Kaminski, and Antoine Picard. And finally thanks to Google and my director Maggie Johnson for the enlightened generosity to put these materials out on the internet for free under the Creative Commons Attribution 2.5 license -- share and enjoy!'''
length=len(article)
print(length)

cleaned=article.replace("\n", " ") #replaces newline characters with spaces ) #splits the article into sentences based on period followed by a space (not a perfect solution, but works for this example)
sentences=cleaned.split(". ") #splits the article into sentences based on period followed by a space (not a perfect solution, but works for this example)
print(len(sentences))
for sentence in sentences:
    print(sentence)
    print("---")

words=cleaned.lower().split() #splits the article into words based on spaces and converts them into lowercase
freq={}
for w in words:
    w = w.strip(string.punctuation) #removes punctuation from the beginning and end of each word
    if w:
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
        score += freq.get(w, 0) #adds the frequency of each word in the sentence to the score
    if (len(words_in_sentence))>0:
        avg_score = score / len(words_in_sentence) #calculates the avg score for the sentence by dividing the score by the length of words in the sentence
    else:
        avg_score = 0
    sentence_scores.append((s, avg_score))
sorted_sentences = sorted(sentence_scores, key=lambda x:x[1], reverse = True) #sorts the sentences based on their avg score in the descending order
# lambda is used to create a small, one line function without a name.

top_3 = sorted_sentences[:3] #gets the top 3 sentences with highest avg score
for s, score in top_3:
    print(round(score,2), "->",s)