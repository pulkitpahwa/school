from django.db import models

class Holidays(models.Model):
	date  = models.IntegerField()
	month = models.CharField(max_length = 12)
	year = models.IntegerField()
	occassion = models.CharField(max_length = 120)

	def __unicode__(self):
		return self.occassion
	class Meta : 
		verbose_name_plural = "Notice for Holiday"


class Prospective_student(models.Model):
	notice = models.CharField(max_length = 200)

	class Meta : 
		verbose_name_plural = "Notice for prospective students"

	
class current_student(models.Model) :
	notice = models.CharField(max_length = 200)

	class Meta  :
		verbose_name_plural = "Notive for current students"

class Event(models.Model):
	event_name = models.CharField(max_length = 200)
	date = models.IntegerField()
	month = models.CharField(max_length = 12)
	year = models.IntegerField()

	class Meta : 
		verbose_name_plural = "Notice for upcoming events"

class Exam_rule(models.Model):
	p1 = models.TextField("Introduction",max_length = 1000,null= True,blank = True)
	h1 = models.CharField("Heading1",max_length = 150,null = True,blank = True)
	p2 = models.TextField("Exam Rules",max_length = 4000,null = True,blank = True)

	class Meta :
		verbose_name_plural = "Rules for examinations"

class Title(models.Model):
	a = models.CharField("",max_length = 120)
	b = models.CharField("",max_length = 120)
	c = models.CharField("",max_length = 120)
	d = models.CharField("",max_length = 120)
	e = models.CharField("",max_length = 120)
	f = models.CharField("",max_length = 120)
	g = models.CharField("",max_length = 120)
	h = models.CharField("",max_length = 120,null = True)
	i = models.CharField("",max_length = 120,null = True,blank = True)
	j = models.CharField("",max_length = 120,null = True, blank = True)
	k = models.CharField("",max_length = 120,null = True, blank = True)
	l = models.CharField("",max_length = 120,null = True, blank = True)



