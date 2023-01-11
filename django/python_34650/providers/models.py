from django.db import models

class Provider(models.Model):
    CONDITION_CHOICES = (
        ('monotributista', 'monotributista'),
        ('responsable inscripto', 'responsable inscripto'),
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    condition = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.email}' 

