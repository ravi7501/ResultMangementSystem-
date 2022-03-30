from django.shortcuts import render
from .forms import InputForm

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


from .models import Students 


from django.http import HttpResponse
from django.views.generic import View

 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 

from django.template.loader import render_to_string



def index(request):
	return render(request, "index.html")
# Create your views here.

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "student.html", context)


#Creating our view, it is a class based view
"""class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('index.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
"""
def request_views(request, *args, **kwargs):
        slno=int(request.GET["Sr_No"])
        data=Students.objects.get(Sr_No=slno)
        open('result/Templates/temp.html',"w").write(render_to_string('index.html',{'data': data}))
        #getting the template
        pdf = render_to_pdf('temp.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')








