from django.db import models

# Create your models here.

class BaseModel(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True) # status: values 0-Deactivated, 1-Active, null-probably untouched yet
	class Meta:
		abstract = True
