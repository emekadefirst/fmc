from user.models import User
from django.db import models
from utils.base_model import BaseModel
from .apartment_model import ApartmentType, ExtraSpace
from django.core.validators import MinValueValidator, MaxValueValidator

WEEKDAYS = [
    ('MON', 'MONDAY'),
    ('TUE', 'TUESDAY'),
    ('WED', 'WEDNESDAY'),
    ('THU', 'THURSDAY'),
    ('FRI', 'FRIDAY'),
    ('SAT', 'SATURDAY'),
    ('SUN', 'SUNDAY')
]

class BookingDetail(BaseModel):
    class STATUS_CHOICES(models.TextChoices):
        NOT_STARTED = "NOT STARTED", "NOT STARTED"
        IN_PROGRESS = "IN PROGRESS", "IN PROGRESS"
        COMPLETED =  "COMPLETED", "COMPLETED"
    class SCHEDULE(models.TextChoices):
        ONE_OFF = "ONE_OFF", "ONE_OFF"
        WEEKLY = "WEEKLY", "WEEKLY"
        BI_WEEKLY = "BI_WEEKLY", "BI_WEEKLY"
        MONTHLY = "MONTHLY", "MONTHLY"
    cleaner = models.ForeignKey(User, related_name='bookingdetail_cleanings', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='bookingdetail_clients', on_delete=models.CASCADE)
    
    apartment = models.ForeignKey(ApartmentType, on_delete=models.CASCADE)
    number_of_room = models.PositiveIntegerField(default=0)
    number_of_bath = models.PositiveIntegerField(default=0)
    schedule = models.CharField(max_length=20, choices=SCHEDULE.choices, default=SCHEDULE.ONE_OFF)
    number_of_days = models.PositiveIntegerField(default=0)
    selected_days = models.CharField(max_length=20, choices=WEEKDAYS)
    extra_spaces = models.ManyToManyField(ExtraSpace, blank=True)
    number_of_extras = models.PositiveIntegerField(default=0, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cleaning_location = models.TextField()
    week_type = models.IntegerField(choices=[(1, "Week 1"), (2, "Week 2"),(3, "Week 3"), (4, "Week 4")], null=True, blank=True)
    day_of_month = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1),  MaxValueValidator(31)])
    weekdays = models.CharField(max_length=12, choices=WEEKDAYS, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.NOT_STARTED)
    payment_statement = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        extras_total = 0
        if self.extra_spaces.exists():
            for extra in self.extra_spaces.all():
                extras_total += extra.price * (self.number_of_extras or 1)

        days_count = 1
        if self.schedule == self.SCHEDULE.WEEKLY and self.selected_days:
            days_count = len(self.selected_days.split(','))
        elif self.schedule == self.SCHEDULE.BI_WEEKLY and self.selected_days:
            days_count = len(self.selected_days.split(',')) * 2
        elif self.schedule == self.SCHEDULE.MONTHLY and self.selected_days:
            days_count = len(self.selected_days.split(',')) * 4

        self.number_of_days = days_count

        if self.number_of_room and self.number_of_bath:
            base_price = self.number_of_days * (
                self.apartment.price + (self.number_of_room * 13) + (self.number_of_bath * 13)
            )
            self.price = base_price + extras_total

        super().save(*args, **kwargs)

    def __str__(self):
        return self.client.username
