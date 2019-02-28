from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'title': 'Django Word Count App'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    print("fulltext: ", fulltext)
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'length': len(wordlist), 'sortedWords': sortedwords })