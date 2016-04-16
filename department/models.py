from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Computer(models.Model):
	DESIGNATION_CHOICES=(
	('Dir', 'Director'),		
	('D', 'Developer'),
	('HR', 'Manager'),
	('P', 'Peon'),
	('SG', 'Security Guard'),
	('SW', 'Sweeper'),	
	)
	
	WORK_PROFILES = (
	('C++', 'C++'),
	('PHP', 'PHP'),
	('JAVA','Core Java'),
	('C#', 'C#'),
	('PY', 'Python'),
	('Non', 'None'),
	)
	name = models.CharField(max_length = 20)
	designation = models.CharField(max_length = 50, choices = DESIGNATION_CHOICES)
	work_profile = models.CharField(max_length =50, choices = WORK_PROFILES)
	salary = models.IntegerField(default = 10)
	address = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name
