from django.urls import path
from . import views

app_name = 'books'  #namespacing so if i make other apps and want to use list and detail i can refer 

urlpatterns = [
    path('', views.books_list, name="list"),
    path('<slug>', views.book_detail, name="detail"),
]
