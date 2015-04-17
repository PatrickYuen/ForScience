from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class posts(models.Model):
	author = models.CharField(max_length = 200)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	slug = models.SlugField(max_length = 200)
	publish = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	objects = EntryQuerySet.as_manager()
	
	def __str__(self):
		return self.title
	
#look it up	
	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]