from django.db import models
from datetime import datetime

class Projects(models.Model):

    options_category = [
        ('MOBILE','Mobile'),
        ('SITES','Sites'),
        ('LANGIN_PAGES','Landing Pages')
    ]

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=15, choices=options_category, default='')
    image = models.ImageField(upload_to='image/%Y/%m/%d/d', blank=True)
    public_project = models.BooleanField(default=True)
    date_publicated = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title
    

class ImageFieldsProject(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('project',upload_to='image')

    def __str__(self):
        return f'Imagem do projeto "{self.project}" adicionada com sucesso!'