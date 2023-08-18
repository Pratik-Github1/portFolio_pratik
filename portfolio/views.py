from django.shortcuts import render
from django.http import HttpResponse
# from .models import ContactModel
from django.contrib import messages

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 

from django.http import FileResponse
from django.conf import settings
import os



from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string


def index(request):
    return render(request , "index.html")


def saveView(request):
    return render(request , "save.html")

def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

# class GeneratePdf_purchase(View):
#      def get(self, request, *args, **kwargs):
#         purchase = Purchase.objects.all().order_by('id')
#         open('templates/temp.html', "w").write(render_to_string('total_purchase_pdf.html', {'purchase': purchase}))
#         # Converting the HTML template into a PDF file
#         pdf = html_to_pdf('temp.html')
#          # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')

class GeneratePdf_Resume(View):
    def get(self, request, *args, **kwargs):
        open('templates/temp.html', "w").write(render_to_string('resume.html'))
        pdf = html_to_pdf('temp.html')
        return HttpResponse(pdf, content_type='application/pdf')
    
def download_resume(request):
    resume_path = os.path.join(settings.MEDIA_ROOT, 'resume\pratik_resume.pdf')
    resume_file = open(resume_path, 'rb')
    response = FileResponse(resume_file , content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    return response