from django.db import models
#adding models for the catalog app
class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.title

    
class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"    


class Product(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    description=models.TextField(blank=True,verbose_name="Description")


    def __str__(self):
        return self.title



class Meta:
    verbose_name="Product"
    verbose_name_plural="Products"

    
class Meta:
    ordering = ['title']
  