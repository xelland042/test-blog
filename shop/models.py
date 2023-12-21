from django.db import models


class Specification(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f'{self.product_id} / {self.id} - {self.title}'


class Category(models.Model):
    category_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.category_id} / {self.id} - {self.title}'


class Type(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.product_id} / {self.id} - {self.title}'


class SubType(models.Model):
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f'{self.type_id} / {self.id} - {self.title}'


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f'{self.id} - {self.title}'
