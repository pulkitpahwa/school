from django.db import models

class Notice(models.Model):
	notice = models.TextField(max_length = 200)

	def __unicode__(self):
		return self.notice
