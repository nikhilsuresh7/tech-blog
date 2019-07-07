from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to='image/', blank=True, null=True)
	content = models.TextField(null=True, blank=True)

	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated', '-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.id}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
