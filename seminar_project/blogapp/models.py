from django.db import models
from datetime import timedelta, date


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(max_length=3000)
    birthdate = models.DateField()

    def __str__(self):
        return f'Имя и фамилия: {self.name} {self.lastname}, email: {self.email}, ' \
               f'age: {(date.today() - self.birthdate) // timedelta(days=365.2425)}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    ispublic = models.BooleanField(default=False)

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'

    def __str__(self):
        return f'Title is {self.title}'


"""class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'
"""