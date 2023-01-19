from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('essay_writing/', views.essay_writing, name='essay_writing'),
    path('paraphrase/', views.paraphrase, name='paraphrase'),
    path('about/', views.about, name='about'),
]
