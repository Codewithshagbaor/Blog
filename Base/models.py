from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save

class User(AbstractUser):
  email = models.EmailField(
    verbose_name='Email Address',
    max_length=255,
    unique=True,
  )
  verified = models.BooleanField(default=False)
  is_complete = models.BooleanField(default=False)
  username = models.CharField(max_length=1000, null=False, unique=True)
  name = models.CharField(max_length=1000, null=False)
  bio = models.TextField()
  location = models.CharField(max_length=1000)
  points = models.PositiveIntegerField(default=0, verbose_name="reputation")
  followers = models.ManyToManyField("self", symmetrical=False, blank=True)
  profile_img = models.ImageField(upload_to='ProfilePicture', null=True)
  
  USERNAME_FIELD = 'username'

  REQUIRED_FIELDS = ['name']
  
  def modify_points(self, added_points):
    self.points += added_points
    self.save()
  
  def __str__(self):
    return self.username

class Verification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  overview = models.TextField()
  file = models.FileField(upload_to='VerificationFiless')

  def __str__(self):
    return self.user.username

class Follow(models.Model):
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
  following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ['follower','following']