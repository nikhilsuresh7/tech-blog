from django import forms

from .models import BlogPost

class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ["title", "image", "content"]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexact=title)

		instance = self.instance
		if instance:
			qs = qs.exclude(title=title)

		if qs.exists():
			raise forms.ValidationError("This title has already been used. Please use a new catchy one.")
		return title