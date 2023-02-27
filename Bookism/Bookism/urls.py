from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from Books import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Books/', include('Books.urls')),
    path('about/', views.about),
    path('', book_views.books_list, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)