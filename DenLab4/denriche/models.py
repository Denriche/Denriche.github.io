from django.db import models
class User(models.Model):
    e_mail = models.EmailField(primary_key=True)
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    shipping_address = models.CharField(
        max_length=256,
    )

class Cart(models.Model):
    cart_code = models.AutoField(primary_key=True)
    total_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )
    num_products = models.IntegerField()
    pay_now = models.BooleanField(

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Product(models.Model):
    prod_code = models.AutoField(primary_key=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    product_name = models.CharField(
        max_length=100,
    )
    description = models.CharField(
        max_length=500,
    )
	
class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Test
		fields = ('url', 'name', 'type')
# Create your models here.
