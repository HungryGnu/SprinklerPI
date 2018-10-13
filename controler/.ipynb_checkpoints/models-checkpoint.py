
from django.db import models

class Zone(models.Model):
    zone_number = models.IntegerField(max_length=64, unique=True)
    pin_number = models.IntegerField(max_length=64)
    zone_name = models.CharField(max_length=64, null=True, blank=True)
    run_duration = models.IntegerField(max_length=64, default=900)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    alternate_days = models.BooleanField(default=False)
    run_next = models.BooleanField(default = False)
    postponed = models.BooleanField(default = False)

    class Meta():
        managed = True

class Record(models.Model):
    delay_choices = (("W", "Weather"),
                    ("M", "Manual"),
                    )
    
    zone_number = models.ForeignKey(Zone, to_field="zone_number", on_delete=models.PROTECT)
    # Date/Time of run
    run_date = models.DateTimeField(auto_now=True)
    # Duration of run
    run_duration = models.IntegerField(max_length=64)
    # Run as scheduled
    on_schedule = models.BooleanField()
    # Run as delay
    as_delay = models.BooleanField()
    # Reason for delay:
    delay_reason = models.CharField(max_length=1, choices=delay_choices, default = 'W')