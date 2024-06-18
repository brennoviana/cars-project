from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = ['login', 'logout', 'register']
        
    def __call__(self, request):
        path = request.path_info
        print(path)
        if not request.user.is_authenticated:
            if path == '/':
                return redirect(settings.LOGIN_URL)
            if (not any(path.startswith(url) for url in ['/static/', '/admin/']) and 
                resolve(path).url_name not in self.exempt_urls):
                return redirect(settings.LOGIN_URL)

        response = self.get_response(request)
        return response
