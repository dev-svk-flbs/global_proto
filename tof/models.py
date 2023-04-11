from django.db import models


class TofData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value1 = models.IntegerField(null=True)
    value2 = models.IntegerField(null=True)
    value3 = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.timestamp} - Value1: {self.value1}, Value2: {self.value2}, Value3: {self.value3}'


class TofData1(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value1 = models.IntegerField(null=True)
    value2 = models.IntegerField(null=True)
    value3 = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.timestamp} - Value1: {self.value1}, Value2: {self.value2}, Value3: {self.value3}'


class TofData2(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value1 = models.IntegerField(null=True)
    value2 = models.IntegerField(null=True)
    value3 = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.timestamp} - Value1: {self.value1}, Value2: {self.value2}, Value3: {self.value3}'


class VizData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value1 = models.IntegerField(null=True)
    value2 = models.IntegerField(null=True)
    value3 = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.timestamp} - Value1: {self.value1}, Value2: {self.value2}, Value3: {self.value3}'

class LdrData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value1 = models.IntegerField(null=True)
    value2 = models.IntegerField(null=True)
    value3 = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.timestamp} - Value1: {self.value1}, Value2: {self.value2}, Value3: {self.value3}'



class IncidentData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=20)
    
    value1 = models.IntegerField(null=True)
    value2 = models.IntegerField(null=True)
    value3 = models.IntegerField(null=True)
    value4 = models.IntegerField(null=True)
    value5 = models.IntegerField(null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    breakAction = models.BooleanField()
    override=models.BooleanField()
    speed = models.FloatField(default=0.0)
    zone_coord1 = models.IntegerField(null=True)
    zone_coord2 = models.IntegerField(null=True)
    zone=  models.IntegerField(null=True)


    def __str__(self):
        return f'{self.timestamp} - Value1: {self.value1}, Value2: {self.value2}, Value3: {self.value3}'



class Device(models.Model):
    DEVICE_TYPES = (
        ('LIDAR', 'Lidar'),
        ('TOF', 'Tof Camera'),
        ('VISUAL', 'Visual Camera'),
        ('OTHERS', 'Others'),
        ('LEGACY', 'Legacy'),
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    status = models.CharField(max_length=10)
    last_seen = models.DateTimeField()

    def __str__(self):
        return self.name


from django.db import models

class AmbientConditions(models.Model):
    RAIN = 'Rain'
    SNOW = 'Snow'
    FOG = 'Fog'
    OTHER = 'Other'
    CONDITION_TYPES = [
        (RAIN, 'Rain'),
        (SNOW, 'Snow'),
        (FOG, 'Fog'),
        (OTHER, 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    condition_type = models.CharField(max_length=10, choices=CONDITION_TYPES)
    outdoor_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    ground_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    other_conditions = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


from django.db import models

class SystemOwner(models.Model):
    organization_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_email = models.EmailField(max_length=255)
    owner_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.organization_name

