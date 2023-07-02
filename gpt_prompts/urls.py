"""gpt_prompts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns
urlpatterns = [
    # URL pattern for admin site
    path('admin/', admin.site.urls),

    # URL pattern for prompts app
    path('', include('prompts.urls')),

    # # URL pattern for accounts app
    # path('accounts/', include('accounts.urls')),
    # allauth
    path('accounts/', include('allauth.urls')),

    # URL pattern for social authentication app
    path('social-auth/', include('social_django.urls', namespace='social')),

    # URL pattern for rosetta app (for translation management)
    # path('rosetta/', include('rosetta.urls')),
]

# Add static and media files to URL patterns if in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)