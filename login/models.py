from django.db import models
from django.contrib.auth.models import User

class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
         
	name = models.ForeignKey(User), models.CharField(max_length=100)  #Like a VARCHAR field
	description = models.TextField() #Like a TEXT field
	createdby = models.CharField(max_length=100,default = 'admin')
	#created = models.DateTimeField() #Like a DATETIME field
	#num = models.ForeignKey(User)
 
	def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
		return self.createdby
