import pdfplumber
from django.shortcuts import render, redirect

#pip install pdfplumber
def plum_daldal(filename):
    st = ""
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            st += page.extract_text()
    return st

def index(request):
    context = {}
    if (request.method == "POST"):
        pdf = request.FILES.get('file')
        context = {
            "text": plum_daldal(pdf)
        }
    return render(request, "rpdf/index.html", context)