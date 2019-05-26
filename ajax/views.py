from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
	return render(request, 'homepage.html')

class SignUpView(CreateView):
	template_name = 'auth/signup.html'
	form_class = UserCreationForm

def validate_username(request):
	username = request.GET.get('username',None)
	data = {
		'is_taken': User.objects.filter(username__iexact = username).exists()
	}
	return JsonResponse(data)