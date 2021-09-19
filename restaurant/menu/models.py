from django.db import models

# Create your models here.
class foodItems(models.Model):
    foodItems_id = models.AutoField
    foodItems_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='menu/images', default="")

    def __str__(self):
        return self.foodItems_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111, null=True, blank=True)
    zip_code = models.CharField(max_length=111, null=True, blank=True)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return f'{self.items_json} {self.zip_code}'

