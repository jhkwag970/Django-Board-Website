from django.shortcuts import render
import googletrans
from googletrans import Translator


# Create your views here.
def index(request):
    context = {}
    if (request.method == "POST"):
        btext = request.POST.get("btext")
        f = request.POST.get("f")
        t = request.POST.get("t")
        
        translator = Translator()
        trans1 = translator.translate(btext, src=f, dest=t)
        context = {
            "text" : trans1.text,
            "f" : f, 
            "t" : t, 
            "btext" : btext,
        }

        #context.update({
        #    "text" : trans1.text,
        #    "f" : f, 
        #    "t" : t, 
        #    "btext" : btext
        #})

    return render(request, "trans/index.html", context)
