from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            if user.password == password:
                return user
        except UserModel.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            user = UserModel.objects.filter(email=username).order_by('id').first()
            if user.password == password:
                return user
            return None
