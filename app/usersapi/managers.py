from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Overriding the default user manager class """
    def create_user(self, email, password=None, **kwargs):
        """The utility function that helps with the creation of new users"""
        if not email:
            raise ValueError("Users must have an email")
        email =self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user 


    def create_superuser(self, email, password, **kwargs):
        """The utility function and cli that helps with the creation of super users"""
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True 
        user.save(using=self._db)
        return user 

