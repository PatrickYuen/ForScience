"""from django.shortcuts import render
from django.shortcuts import render_to_response

from blog.models import posts

# Create your views here.
#from models import posts

def home(request):
	entries = posts.objects.all()[:10]
	return render_to_response('index.html', {'posts': entries})
"""
		
from django.views import generic
from blog.models import posts


class BlogIndex(generic.ListView):
    queryset = posts.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = posts
    template_name = "post.html"