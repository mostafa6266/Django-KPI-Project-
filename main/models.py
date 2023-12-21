from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=30, unique=True)
    day_kpi = models.IntegerField(default=0)
    month_kpi = models.IntegerField(default=0)
    total_kpi = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        update_total_kpi = kwargs.pop('update_total_kpi', True)
        if self.pk:
            old_self = Data.objects.get(pk=self.pk)
            if update_total_kpi:
                day_kpi_diff = self.day_kpi - old_self.day_kpi
                month_kpi_diff = self.month_kpi - old_self.month_kpi
                self.total_kpi += day_kpi_diff + month_kpi_diff
        else:
            # For a new instance, calculate total_kpi normally
            self.total_kpi = self.day_kpi + self.month_kpi

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

  

    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', null=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='data_comments')
    comment = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.comment}'
    
class Responsibilities(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='responsibilities')
    responsible = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.data.name} - {self.responsible}"
    
    