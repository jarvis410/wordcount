from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'count': len(word_list), 'fulltext': fulltext, 'sorted_list': sorted_list})


def about(request):
    return render(request, 'about.html')
