from django.shortcuts import render, redirect
from .models import AudioFile
import mimetypes
import os
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


def index(request):
    audio_file_list = [name_file for name_file in sorted(os.listdir('media/'))]
    if request.method == 'POST':
        uploaded_file = request.FILES.get('audioFiles')
        if uploaded_file:
            if uploaded_file.name in audio_file_list:
                messages.error(request, 'This file already exists in the list')
                return redirect('index')
            uploaded_mime_type = mimetypes.guess_type(uploaded_file.name)[0]
            if uploaded_mime_type and uploaded_mime_type.startswith('audio'):
                fs = FileSystemStorage()
                fs.save(uploaded_file.name, uploaded_file)
                return redirect('index')
            else:
                uploaded_file.close()
                messages.error(request, 'This is not an audio file')
                return redirect('index')
    if not os.path.exists('/media/'):
        os.makedirs('/media/')
    audio_file_list_p = [AudioFile(name_file) for name_file in audio_file_list]
    audio_dic = {
        'audio_file_list': audio_file_list_p
    }
    return render(request, 'audio_files/index.html', audio_dic)
