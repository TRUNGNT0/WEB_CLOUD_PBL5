from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'custom_user'

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    planted_date = models.DateField()
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='plants')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'plants'

class PlantStatus(models.Model):
    # Liên kết với cây
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='statuses')
    
    # Các trường trạng thái
    temperature = models.FloatField()  # Nhiệt độ
    humidity = models.FloatField()  # Độ ẩm
    light = models.FloatField()  # Ánh sáng
    
    # Tình trạng cây (dùng Choice để giới hạn giá trị)
    CONDITION_CHOICES = [
        ('GOOD', 'Tốt'),
        ('sick', 'Bệnh'),
        ('WILTED', 'Héo'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='GOOD')
    
    # Thời gian ghi nhận
    timestamp = models.DateTimeField(auto_now_add=True)  # Tự động lưu thời gian khi tạo

    def __str__(self):
        return f"Status of {self.plant.name} at {self.timestamp}"

    class Meta:
        db_table = 'plant_statuses'  # Tên bảng trong database
        ordering = ['-timestamp']  # Sắp xếp theo thời gian mới nhất trước