from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image
import re
from io import BytesIO


# Create your views here.
def main(request):
    return render(request,"main.html")
def starting(request):
    return render(request,"starting.html")
def registering(request):
    return render(request,"registering.html")
@csrf_exempt
def finding(request):
    if request.method == 'POST':
        # Retrieve the image data from the form
        image_data = request.POST.get('image_data')

        # Remove the data URL scheme part
        image_data = re.sub('^data:image/.+;base64,', '', image_data)

        # Decode the Base64 string
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        image.show()  
        return JsonResponse({'status': 'success', 'message': 'Image uploaded successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


