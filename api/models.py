from mongoengine import *
connect('mydb')

# Create your models here.

class Orders(models.Model):
    OrderID = models.IntegerField()
    CustomerID = models.CharField(max_length=255, blank=False, unique=True)
    EmployeeID = models.IntegerField()
    OrderDate = models.DateTimeField()
    RequiredDate = models.DateTimeField()
    ShippedDate = models.DateTimeField()
    ShipVia = models.IntegerField()
    Freight=models.FloatField()
    date_created=models.DateTimeField()
    date_modified=models.DateTimeField()
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)