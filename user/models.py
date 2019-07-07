from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
	
	def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("Users must have an email")
		if not full_name:
			raise ValueError("Users must have a full name")
		if not password:
			raise ValueError("Users must have a password")

		user = self.model(
			email = self.normalize_email(email),
			full_name = full_name,
	 		)
		user.set_password(password)

		user.active = is_active
		user.staff = is_staff
		user.admin = is_admin
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, full_name, password=None):
		user = self.create_user(
			email,
			full_name,
			password = password,
			is_staff = True
			)
		return user

	def create_superuser(self, email, full_name, password=None):
		user = self.create_user(
			email,
			full_name,
			password = password,
			is_staff = True,
			is_admin = True
			)
		return user

class User(AbstractBaseUser):
	full_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)

	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["full_name"]

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.full_name

	def has_module_perms(self, app_label):
		return True

	def has_perm(self, perm, obj=None):
		return True	

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active