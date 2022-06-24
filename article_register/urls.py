from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.article_form,name='article_insert'),
    path('<int:id>/', views.article_form,name='article_update'),
    path('delete/<int:id>/',views.article_delete,name='article_delete'),
    path('list/',views.article_list,name='article_list')
]