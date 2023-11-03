from django.urls import path
from . import views

app_name = 'Dobak'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('<int:match_id>/', views.detail, name='detail'),
    path('<int:match_id>/results/', views.results, name='results'),
    path('<int:match_id>/vote/', views.vote, name='vote'),
] 
