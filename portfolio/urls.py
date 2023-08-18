from django.urls import path
from portfolio import views
from .views import  GeneratePdf_Resume 
urlpatterns = [
    path('' , views.index , name="index"),
    path('save/' , views.saveView , name="save") ,
    path("resume/pdf" , GeneratePdf_Resume.as_view() , name="resume/pdf") ,
    path('download/resume/', views.download_resume, name='download_resume'),
]