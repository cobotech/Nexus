from django.db import models

# Create your models here.
class StockItem(models.Model):
    name = models.CharField("商品名",max_length=100),
    product_code = models.CharField("商品コード",max_length=20,unique=True,null=True,blank=True)
    quantity =models.DecimalField("数量",max_digits=10,decimal_places=2)
    unit = models.CharField("単位",max_length=20)
    created_at =models.DateTimeField("作成日",auto_now_add=True)
    updated_at = models.DateTimeField("更新日",auto_now=True)

def __str__ (self):
    return f"{self.name} ({self.quantitiy} {self.unit})"