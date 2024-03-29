from django.db import models

MODES = (
    ('full', 'Full'),
    ('custom', 'Custom'),
)

class Seed(models.Model):
  hash = models.CharField(max_length=10, unique=True)
  seed = models.BigIntegerField()
  version = models.CharField(max_length=16)
  game_name = models.CharField(max_length=32)
  prefix = models.CharField(max_length=16)
  generated = models.DateTimeField(auto_now_add=True)
  mode = models.CharField(max_length=16, choices=MODES)
  debug_mode = models.BooleanField(default=False)
  flags = models.TextField()


class Patch(models.Model):
  seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
  sha1 = models.CharField(max_length=40)
  patch = models.TextField()

  class Meta:
    unique_together = [('seed')]
