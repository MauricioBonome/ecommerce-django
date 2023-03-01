from django.db import models
from django.urls import reverse

class category (models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image= models.ImageField(upload_to= 'photos/categories',blank=True)
   
   #esto es para modificar los nombres hay que migrarlos, tambien migramos todo lo que esta models.
   
    class Meta:
        verbose_name = 'category'
        verbose_name_plural ='categories'

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self) -> str:
        return self.category_name