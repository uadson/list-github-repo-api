from django.contrib.auth.models import AbstractUser


<<<<<<< HEAD
class User(AbstractUser):
    pass
=======
class Base(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		abstract = True

class Repository(Base):
	name = models.CharField('Name:', max_length=200)
	url = models.URLField('URL:', max_length=200)
>>>>>>> main
