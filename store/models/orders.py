from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return ' {}'.format(self.product.name)


    def placeOrder(self):
        p1=Product()
        act_stock=p1.stock
        order_stock=self.quantity
        final_stock=act_stock-order_stock
        p1.stock=final_stock
        p1.save()
        print("stock:",p1.stock)
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

