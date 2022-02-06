from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from applications.models import Customer, Employee

class UserAccountManager(BaseUserManager):
    """Handles User Creation"""
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        # user.save(using=self._db) if more than one DB
        user.save()
        if "engineer" in str(user.email):
            Employee.objects.create(employee_id=user.id,role="Engineer",)
        elif "designer" in str(user.email):
            Employee.objects.create(employee_id=user.id,role="Designer",)
        elif "busdevclerk" in str(user.email):
            Employee.objects.create(employee_id=user.id,role="Busdevclerk",)
        else:
            Customer.objects.create(customer_id=user.id,)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """Database model for the User Account"""
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

