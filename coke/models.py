from django.db import models

class Notice(models.Model):
	notice = models.TextField(max_length = 200)

	def __unicode__(self):
		return self.notice

class Academic(models.Model):
	list = models.TextField("Academic information",max_length = 30000)

	def __unicode__(self):
		return self.list[0:30]

class Parent_Information(models.Model):
	info = models.TextField("Information for parents",max_length = 2000)
	
	def __unicode__(self):
		return self.info[0:30]

class faculty(models.Model):
	name = models.CharField("Name of Faculty",max_length = 30)
	designation =  models.CharField("Designation",max_length = 15)
	qualification = models.CharField("Qualification",max_length = 15)
 
	def __unicode__(self):
 		return self.name,self.qualification


