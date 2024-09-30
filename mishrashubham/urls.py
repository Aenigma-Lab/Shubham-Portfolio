"""
URL configuration for mishrashubham project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from mishrashubham import views



from django.contrib import admin
from django.urls import path,include, re_path
from mishrashubham import views  # Single import statement for views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.home_page, name='homepage'),  # Home page
    path('index-2/', views.homePage_2, name='homepage-2'),  # Alternate home page
    path('404/', views.custom_404_view, name='page404'),  # Custom 404 page
    path('contact/', views.contact_us, name='contact-us'), # Contact us page
    path('portfolio/',views.portfolio, name='portfolio'), #Portfolio
    path('portfolio-single/', views.portfolio_single, name='portfolio-single'),  # Portfolio item 1
    path('portfolio-single-2/', views.portfolio_single_2, name='portfolio-single-2'),  # Portfolio item 2
    path('blog/', views.my_blog, name='my-blog'),  # Blog page
    path('blog-single/', views.blog_single, name='blog-single'),  # Blog page
    path('resume/', views.resume, name='resume'),  # Resume page
    path('contact-us-submit/', views.contact_us_submit, name='contact-us-submit'),
    path('success-page/', views.success_page, name='success-page'), 

]
