from django.urls import path

from .views import SongUploadView

app_name = 'song_dashboard'

#This pattern maps the URL "upload/" relative to the app's base URL.
# When a user accesses this URL, it will invoke the SongUploadView view class to handle the request.
# The .as_view() method is used to convert the view class into a callable view function.
# The name parameter is set to 'song_upload' to provide a unique name to this URL pattern. It can be used to reverse-resolve this URL in the application's code.

urlpatterns = [
    path('upload/', SongUploadView.as_view(), name='song_upload'),
]
