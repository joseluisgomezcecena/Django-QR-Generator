from django.db import models


# Create your models here.
class QrCode(models.Model):
    part_number = models.CharField(max_length=1000)
    work_order = models.CharField(max_length=1000)
    quantity = models.FloatField()
    img_url = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return the work order number and part number

    def __str__(self):
        return str(self.work_order) + ' - ' + str(self.part_number)





class DjangoPartNumbers(models.Model):
    part_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'django_part_numbers'

    def __str__(self):
        return str(self.part_number)
