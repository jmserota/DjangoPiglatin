from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):

    original = request.GET['plaintext']
    translated=''

    for word in original.split():
        if(word[0] in ['a','e','i','o','u']):
            #first letter is a vowel
            translated+=word+'yay '
        else:
            #first letter is a consonant
            translated+=word[1:]+word[0]+'yay '

    # return HttpResponse(translated)
    return render(request, 'translate.html', {'original': original, 'translation':translated})

def about(request):
    return render(request, 'About.html')