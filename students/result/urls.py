from django.urls import path

from result import views

#from .views import GeneratePdf

urlpatterns=[
      
    
    path("",views.home_view),
    path('index.html',views.index, name="home"),
    #path("pdf/",views.some_view) ,path("pdf/",GeneratePdf.as_view()),
    path("request",views.request_views)
]