
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from partners import views as partners_views
from contact import views as contact_views
from blog import views as blog_views
from dashboard import views as dashboard_views
from projects import views as projects_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('impact/', views.impact, name='impact'),
    path('projects/', projects_views.projects, name='projects'),
    path('partners/', partners_views.partners, name='partners'),
    path('news/', blog_views.news, name='news'),
    path('news/<slug:slug>/', blog_views.news_detail, name='news_detail'),
    path('contact/', contact_views.contact, name='contact'),
    path('partner/', partners_views.partner, name='partner'),

    path('dashboard/login/', dashboard_views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', dashboard_views.dashboard_logout, name='dashboard_logout'),
    path('dashboard/', dashboard_views.dashboard_home, name='dashboard_home'),
    path('dashboard/<str:model_slug>/', dashboard_views.model_list, name='dashboard_model_list'),
    path('dashboard/<str:model_slug>/new/', dashboard_views.model_create, name='dashboard_model_create'),
    path('dashboard/<str:model_slug>/<int:pk>/', dashboard_views.model_detail, name='dashboard_model_detail'),
    path('dashboard/<str:model_slug>/<int:pk>/edit/', dashboard_views.model_edit, name='dashboard_model_edit'),
    path('dashboard/<str:model_slug>/<int:pk>/delete/', dashboard_views.model_delete, name='dashboard_model_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
