from django.shortcuts import render
from django.shortcuts import render_to_response

from blog.models import posts

# Create your views here.
#from models import posts

def home(request):
	entries = posts.objects.all()[:10]
	return render_to_response('index.html', {'posts': entries})