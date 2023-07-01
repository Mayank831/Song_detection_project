from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     #The first URL pattern (path('admin/', admin.site.urls)) maps the URL "admin/" to the Django admin site.
    path('admin/', admin.site.urls),

   #The second URL pattern (path('dashboard/', include('song_dashboard.urls', namespace='song_dashboard'))) maps the URL "dashboard/" to the URLs defined in the "song_dashboard" app. The include() function is used to include the URL patterns from the "song_dashboard.urls" module. The namespace parameter is used to provide a namespace for the included URLs.
    path('dashboard/', include('song_dashboard.urls', namespace='song_dashboard')),
   
]

# The if settings.DEBUG block checks if the project is in debug mode.

# If the project is in debug mode, the urlpatterns list is updated to include a URL pattern for serving media files. The static() function is used to configure the URL pattern for serving media files based on the MEDIA_URL and MEDIA_ROOT settings specified in the project's settings module.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)