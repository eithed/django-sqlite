from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=60)

	@classmethod
	def create(cls, title):
		page = cls(title=title)
		return page