
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from partners import views as partners_views
from contact import views as contact_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('impact/', views.impact, name='impact'),
    path('projects/', views.projects, name='projects'),
    path('partners/', partners_views.partners, name='partners'),
    path('news/', blog_views.news, name='news'),
    path('news/<slug:slug>/', blog_views.news_detail, name='news_detail'),
    path('contact/', contact_views.contact, name='contact'),
    path('partner/', partners_views.partner, name='partner'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
