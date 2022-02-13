from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=230)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='Book', on_delete=models.CASCADE)
    author = models.CharField(max_length=100 , null=True)
    isbn  = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    imageurl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title
    

class products(models.Model):
    product_tag  = models.CharField(max_length=20)
    name = models.CharField(max_length=230)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    imageurl = models.URLField()
    status = models.BooleanField(default = True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Products'


    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag , self.name)
        