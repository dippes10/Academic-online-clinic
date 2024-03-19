from django.db import models
import uuid

class Record(models.Model):
    unique_patient_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    employer = models.CharField(max_length=100, blank=True, null=True)
    insurance_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
