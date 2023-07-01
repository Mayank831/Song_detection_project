import tempfile
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import File
import librosa
import io
#The pydub module is imported for audio file manipulation.
from pydub import AudioSegment
import os


#Inside the SongUploadView class, there is a get() method defined. This method is called when a GET request is made to the corresponding URL.
class SongUploadView(View):
    def get(self, request, *args, **kwargs):
        #The File objects are retrieved from the database using File.objects.filter(user='End User'), filtering files belonging to the 'End User'.
        files = File.objects.filter(user='End User')

        #The total duration of all the files is calculated using a generator expression and the sum() function.
        total_duration = sum(file.duration for file in files)


        warning = total_duration > 600  # Check if total duration exceeds 10 minutes
        #The render() function is responsible for rendering the HTML template with the provided context variables and returning the resulting HTML response.
        return render(request, 'song_dashboard/song_upload.html', {'files': files, 'warning': warning})
    
    
    def post(self, request, *args, **kwargs):

        #The uploaded_files variable is assigned the value of request.FILES.getlist('files'). This retrieves a list of all uploaded files with the input name 'files' from the request object.
        # A loop is started to iterate through each uploaded_file in the uploaded_files list.
        uploaded_files = request.FILES.getlist('files')
        for uploaded_file in uploaded_files:
            # Perform song detection here
            is_song , duration=  self.detect_song(uploaded_file)

            # Calculate the duration using librosa
            # duration = self.calculate_duration(uploaded_file)

            # Create a new File instance and save it to the database
            file = File(
                file=uploaded_file,
                user='End User',
                size=uploaded_file.size,
                extension=uploaded_file.name.split('.')[-1],
                duration=  duration,  # Set the actual duration based on the audio file
                is_song=is_song
            )
            #The save() method is called on the file object to save it to the database.
            file.save()

            #After processing all uploaded files, a JSON response is returned with the key 'success' set to True to indicate that the upload process was successful.

        return JsonResponse({'success': True})
    
     


    def detect_song(self, uploaded_file):
        # Set the maximum allowed duration in seconds
        max_duration = 600

        # Read the file content from the uploaded file object
        file_content = uploaded_file.read()

        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(file_content)
        temp_file.close()

       
            # Load the audio file using pydub
        # Load the audio file using librosa
        audio, sr = librosa.load(io.BytesIO(file_content))

        # Calculate the duration of the audio in seconds
        duration = librosa.get_duration(y=audio, sr=sr)


        if duration > max_duration:
                return 0, 0  # Not a song, duration exceeds the limit
        else:
                return 1, duration  # Song, return the actual duration
       
         
# ...

    

    

# ...

     

        
    def calculate_duration(self, uploaded_file):

        #here i treid to convert the format of song but for some reason it didnt work
        
        # audio = AudioSegment.from_file(uploaded_file.temporary_file_path(), format='mp3')
        # wav_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        # wav_file.close()
        # audio.export(wav_file.name, format='wav')


    # Load the audio file using librosa directly from the temporary file
        audio, sr = librosa.load(uploaded_file)

        # Calculate the duration of the audio in seconds
        duration = librosa.get_duration(audio, sr=sr)

        # Delete the temporary WAV file
        # os.remove(wav_file.name)


        return duration


        
     

   

    