from django.db import models
from django.contrib.auth.models import User

class UserExtend(User):
    productImage=models.ImageField(upload_to="avater",default="")