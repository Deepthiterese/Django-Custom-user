# accounts/views.py
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.views import View
from .forms import CustomLoginForm
from .models import CustomUser

class CustomLoginView(View):
    def get(self, request):
        
        form_html = """
        <form method="post" action="/accounts/login/">
            <label for="username">Username:</label>
            <input type="text" name="username" id="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password"><br><br>
            <button type="submit">Login</button>
        </form>
        """
        return HttpResponse(form_html)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            if user.user_type == 'admin':
                return HttpResponse("Welcome, Admin!")
            elif user.user_type == 'staff':
                return HttpResponse("Welcome, Staff!")
            else:
                return HttpResponse("Welcome, Customer!")
        else:
            return HttpResponse("Invalid credentials. Please try again.")
