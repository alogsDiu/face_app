from django.shortcuts import render,HttpResponse

def load_tab(request, tab_name, tkn):
    if tab_name == 'tp':
        return load_tp(request,tkn)
    elif tab_name == 'home':
        return load_home(request, tkn)
    elif tab_name == 'profile':
        return load_profile(request,tkn)
    else:
        return HttpResponse('Tab not found', status=404)

def load_home(request,tkn):
    #do some stuff with token
    
    return render(request, 'tabs/home.html')

def load_tp(request,tkn):
    #do some stuff with token
    
    return render(request, 'tabs/tp.html')

def load_profile(request,tkn):
    #do some stuff with token

    return render(request, 'tabs/profile.html')