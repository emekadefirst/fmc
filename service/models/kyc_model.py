from django.db import models
from user.models import User
from utils.base_model import BaseModel

class UserKYCProfile(BaseModel):
    class STATUS(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        DECLINED = 'declined', 'Declined'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    id_image = models.ImageField(upload_to="ID image")
    resume = models.FileField(upload_to="Resume")
    id_document = models.FileField(upload_to="Resume")
    status = models.CharField(max_length=15, choices=STATUS.choices, default=STATUS.PENDING, blank=True)


