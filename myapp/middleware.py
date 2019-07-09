from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import *
from django.contrib.auth.models import User

import datetime 


class SampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        a = ['/login','/register','/auth','/admin']
        for x in a:
            if request.path.startswith(x):
                return None
        if not request.user.is_authenticated:        
            return redirect(settings.LOGIN_URL)


class AutoLogout:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            
            current_datetime = datetime.datetime.now()
            if 'last_login' in request.session :
                last = (current_datetime - request.session['last_login']).seconds
                if last > settings.SESSION_IDLE_TIMEOUT:
                    logout(request)
                    return HttpResponseRedirect('/')
            else:
                request.session['last_login']=current_datetime
        return None        
       
