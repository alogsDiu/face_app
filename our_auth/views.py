from django.shortcuts import render, redirect
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
        name = check(image)
        if name == "":
            return render(request,"registering.html",{image_data:image_data})
        else :
            token = name
            return render(request,"home.html",{token:token, name:name})
    
    return redirect('starting')

def check(image):
    allThePics = []
    for name, pics in allThePics:
        if pics == image:
            return name

    return ""
