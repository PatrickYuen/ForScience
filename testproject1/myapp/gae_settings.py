from blog.models import posts

FIELD_INDEXES = {
	posts: {'indexed': ['title']},
}