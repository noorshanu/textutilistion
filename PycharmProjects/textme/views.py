# i have created a webserver - noor
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
       return render(request,'index.html')

def aboutus(request):
       return render(request,'aboutus.html')
  
  

def analyze(request):
   
    djtext = request.GET.get('text','default')
    #check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    charcount = request.GET.get('charcount','off')
  #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&&_~'''
        analyzed = ""
        for char in djtext:
              if char not in punctuations:
                    analyzed = analyzed + char
                    
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render (request,'analyze.html',params)


    elif(fullcaps=="on"):
          analyzed = ""
          for char in djtext:
                analyzed = analyzed+char.upper()


          params = {'purpose':'Change to Uppercase','analyzed_text':analyzed}
          return render (request,'analyze.html',params)

    elif(newlineremover=="on"):
      analyzed=""
      for char in djtext:
            if char !="\n":
               analyzed = analyzed + char

               params = {'purpose':'Removed Newlines','analyzed_text':analyzed}
               return render (request,'analyze.html',params)
    elif(charcount=="on"):
      analyzed=""
      for char in djtext:
          if char =="analyazed":
              analyzed = analyzed + char

              params = {'purpose':'Removed Newlines','analyzed_text':analyzed}
              return render (request,'analyze.html',params)


    else:
          return HttpResponse("Error")
        
      