
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include("dataentry.urls")),

    path('', views.home, name='home'),
    path('celery-test/', views.celery_test)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)