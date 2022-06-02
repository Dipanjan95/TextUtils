# I make this file
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # params = {'Name':'Dipanjan','Job':'ML Engineer'}
    # return HttpResponse('''<h1>Hello World</h1> <a href="https://www.lockheedmartin.com/">Lockheed Martin</a> ''')
    return render(request,'index.html')

# def about(request):
#     return HttpResponse("<h1>This is my First project</h1>")
#
def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))
def analyze(request):
    djtext=request.POST.get('text','default')
    # print(djtext)
    rempunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlinerem = request.POST.get('newlinerem', 'off')
    extraspacerem = request.POST.get('extraspacerem','off')
    charcount = request.POST.get('charcount','off')
    if rempunc == "on":
        # print(rempunc)
        # analyzed = djtext
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ""
         for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char
         params = {'purpose':'Removed punctuations','analyze_text': analyzed}
         djtext = analyzed
         # return render(request,'analyze.html',params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlinerem == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspacerem == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if (djtext[index]== " " and djtext[index+1]=="  "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount == "on":
        count = len(djtext)
        # for i in djtext:
        #     count = count+1;
        analyzed = 'You have ',count,' characters'
        params = {'purpose': 'Counting the characters', 'analyze_text': analyzed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")
    if(fullcaps!="on" and newlinerem!="on" and extraspacerem!="on"):
        return HttpResponse("Plz select any operation and try again")

    return render(request,'analyze.html',params)
# def capfirst(request):
#     return HttpResponse("<h3>First latter is capitalized</h3>")
#
# def newlineremove(request):
#     return HttpResponse("<h4>New line has been removed</h4>")
#
# def spaceremove(request):
#     return HttpResponse("<h5>space remover</h5><a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("<h6>Character is counted</h6>")


