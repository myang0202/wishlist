from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime


class UserManager(models.Manager):
    def loginValidation(self, username, password):
        errors = []
        if len(User.objects.filter(username=username)) == 0:
        	errors.append("Username does not exist in database")
        else:
        	user = User.objects.get(username=username)
        	hashed = user.password
        	password = password.encode('utf-8')
        	hashed = hashed.encode('utf-8')
        	if not bcrypt.hashpw(password, hashed) == hashed:
        		errors.append("Invalid Password")
        return errors
    def getErrors(self, name, username, password, confirm_password, date):
        errors = []
        if len(name) < 3 :
            errors.append("Name is not valid (needs to be more than 2 characters and only alpha characters)")
        if len(username) < 3:
            errors.append("username must be more than 2 characters")
        if len(password) < 8:
            errors.append("Password needs to be at least 8 characters long")
        if not password == confirm_password:
            errors.append("Passwords must match")
        if len(User.objects.filter(username=username)) > 0:
            errors.append("That username is already taken")
        if len(date) < 1:
            errors.append("date cannot be blank")
        return errors
    def encrypt(self, password):
        password = password.encode('utf-8')
        return bcrypt.hashpw(password, bcrypt.gensalt())
	def validPassword(self, password, hashed):
		password = password.encode('utf-8')
		hashed = hashed.encode('utf-8')
		if bcrypt.hashpw(password, hashed) == hashed:
			return True
		else:
			return False
class User(models.Model):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=155)
    username = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(default="")
    userManager = UserManager()
    objects = models.Manager()
