from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


def analyze(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = request.POST.get('removepun', 'off')
    fullcapital = request.POST.get('fullcapital', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    spaceremover = request.POST.get('extraspacerem', 'off')
    print(removepunc)
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    analysed = ""
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analysed = analysed+char

        params = {'purpose': 'remove puntioations', 'analyzed_text': analysed}
        return render(request, 'analyze2.html', params)

    elif fullcapital == 'on':
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose': 'capitalise', 'analyzed_text': analysed}
        return render(request, 'analyze2.html', params)

    elif newlinerem == 'on':
        for char in djtext:
            if char != '\n':
                analysed = analysed+char
        params = {'purpose': 'new line remover', 'analyzed_text': analysed}
        return render(request, 'analyze2.html', params)

    elif spaceremover == 'on':
        for Index, char in enumerate(djtext):
            if Index == len(djtext)-1:
                break
            if djtext[Index] == ' ' and djtext[Index+1] == ' ':
                pass
            else:
                analysed = analysed + char
        params = {'purpose': 'extra space remover', 'analyzed_text': analysed}
        return render(request, 'analyze2.html', params)

    else:
        return HttpResponse('error')
