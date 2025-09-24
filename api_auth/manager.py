from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazzy as _


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError : 
            raise ValueError (_('Veuillez sasir un email'))
        
    def create_user(self, email, first_name, last_name, password, **extra_fields ):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            if not first_name:
                raise ValueError(_('Le nom doit etre valide '))
            if not last_name:
                raise ValueError (_('Le prenom n\'est pas valide'))
            if not last_name:
                raise ValueError(_("Le prenom n'est pas valide"))
            user = self.model(email = email, first_name = first_name, last_name = last_name, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user 