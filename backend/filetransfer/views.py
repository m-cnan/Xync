from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        
        save_path = os.path.join('received_files', file.name)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully'})
    
    return JsonResponse({'status': 'error', 'message': 'No file received'}, status=400)
