from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    العنوان = models.CharField(max_length=70)
    المحتوى = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.العنوان

    def get_absolute_url(self):
    	return reverse('blog:post', kwargs={'pk':self.pk})


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	content = models.CharField(max_length=300)

	def __str__(self):
		return self.content
    

