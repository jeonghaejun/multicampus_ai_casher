from django.db import models
from django.urls import reverse

class Product(models.Model):
    Name       = models.CharField(verbose_name='Product_name', max_length=50)
    Price      = models.DecimalField(verbose_name='Price', max_digits=7, decimal_places=0)
    Qty        = models.DecimalField(verbose_name='Qty', max_digits=4, decimal_places=0)
    num_sum    = models.DecimalField(verbose_name='Sum', max_digits=11, decimal_places=0)
    
    def __str__(self):
        return self.Name

    def get_absolute_url(self):              # 현재 데이터의 절대 경로 추출
        return reverse('board:detail', args=(self.id,))

    def get_previous(self):                  # 이전 데이터 추출
        return self.get_previous_by_modify_dt()

    def get_next(self):                      # 다음 데이터 추출
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



