from django.db import models
from ..users.models import User

# Create your models here.
class WishManager(models.Manager):
    def getErrors(self,item):
        errors = []
        if len(item) == 0 :
            errors.append("item cannot be blank")
        elif len(item) < 4 :
            errors.append("item is not valid (needs to be more than 3)")
        return errors
class Wish(models.Model):
    item = models.TextField(max_length=255)
    creator = models.ForeignKey(User, related_name="creator")
    otherusers = models.ManyToManyField(User, related_name="otherusers")
    created_at = models.DateTimeField(auto_now_add=True)
    wishManager = WishManager()
    objects = models.Manager()
