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
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        user_name = request.POST.get('username').strip()
        if image_data == None:
            return redirect('starting')
        if user_name=="" or userNameExists(user_name):
            return render(request,"registering.html",{"image_data":image_data,"user_name_exists":True})
        # Remove the data URL scheme part
        image_data = re.sub('^data:image/.+;base64,', '', image_data)

        # Decode the Base64 string
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
    
        # Some database stuff
        
        image.save("faces/ex.png")

        return render(request,"home.html",{"token":"someGeneratedToken"})
    return redirect('starting')

@csrf_exempt
def finding(request):
    if request.method == 'POST':
        # Retrieve the image data from the form
        image_data = request.POST.get('image_data')
        pure_data = image_data
        # Remove the data URL scheme part
        image_data = re.sub('^data:image/.+;base64,', '', image_data)

        # Decode the Base64 string
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        name = check(image)
        if name == "":
            return render(request,"registering.html",{"image_data":pure_data})
        else :
            token = name
            return render(request,"home.html",{token:token, name:name})
    
    return redirect('starting')


from deepface import DeepFace
import numpy as np

def check(image):
    
    #some database stuff

    imageFromDatabase=Image.open('faces/ex.png')
    
    if imageFromDatabase == None:
        return ""
    
    image = image.convert('RGB')
    imageFromDatabase = imageFromDatabase.convert('RGB')

    img1_array = np.array(image)
    img2_array = np.array(imageFromDatabase)

    # Perform face verification
    result = DeepFace.verify(img1_array, img2_array, enforce_detection=False)

    if result['verified'] == True:
        return "imageOwnerNick"
    else :
        return ""

def userNameExists(username):
    #some database stuff
    return False