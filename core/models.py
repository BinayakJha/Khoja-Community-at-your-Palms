from django.db import models
from datetime import date

class Eca(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    theme = models.CharField(max_length=100, default='default')
    message = models.TextField()
    questions = models.TextField(max_length=100, default='')
    online_or_offline = models.CharField(max_length=100, default='online')
    happening_date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        super(Eca, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'ECA'
        verbose_name_plural = 'ECAs'

class EcaApply(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    eca = models.ForeignKey(Eca, on_delete=models.CASCADE)
    questions_answer = models.TextField(max_length=100, default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'ECA Apply'
        verbose_name_plural = 'ECAs Apply'