# Create your views here.
from django.views import generic
from blog.models import posts


class BlogIndex(generic.ListView):
	model = posts
	#queryset = posts.objects.published()
	template_name = "home.html"
	paginate_by = 2