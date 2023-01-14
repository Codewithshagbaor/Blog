from django.db import models
from Base.models import User
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=10000)
  slug = models.SlugField(max_length=250, unique=True)

  def __str__(self):
    return self.name

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=1000000)
  slug = models.SlugField(max_length=1000000, unique=True)
  body = models.TextField()
  image = models.ImageField(upload_to="Posts", null=False)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=False)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)

      if not self.id:
        try:
          points = settings.POINTS_SETTINGS['CREATE_POST']
        except KeyError:
          points = 0
        User.objects.get(id=self.user_id).modify_points(points)
    return super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.comment

  def save(self, *args, **kwargs):
    if not self.post.id:
      try:
        points = settings.POINTS_SETTINGS['CREATE_COMMENT']
      except KeyError:
        points = 0
      User.objects.get(id=self.user_id).modify_points(points)
    return super(Comment, self).save(*args, **kwargs)