from django.db import models


class Starship(models.Model):
    created = models.DateTimeField('Created at', auto_now_add=True)
    updated = models.DateTimeField('Updated at', auto_now=True)

    name = models.CharField('Name', max_length=100, blank=False)
    starship_model = models.CharField('Model', max_length=100, blank=False)
    manufacturer = models.CharField('Manufacturer', max_length=100, blank=False)
    starship_class = models.CharField('Class', max_length=100, blank=False)
    value_when_new = models.IntegerField(
        'Value when new',
        null=True,
        blank=True
    )

    length = models.FloatField('Length', null=False)
    max_atmosphering_speed = models.IntegerField(
        'Maximum Atmosphering Speed',
        null=False
    )
    hyperdrive_capacity = models.FloatField('Hyperdrive Capacity', null=False)
    min_crew = models.IntegerField('Minimum Crew Compliment', null=False)
    max_crew = models.IntegerField('Maximum Crew Compliment', null=False)
    passengers = models.IntegerField('Maximum Passenger Capacity', null=False)
    cargo_capacity = models.IntegerField('Maximum Cargo Capacity', null=False)
    consumables_for = models.CharField(
        'Consumable Capacity For',
        max_length=100,
        blank=False
    )
    mglt = models.IntegerField('Maximum Speed', null=False)

    def __str__(self):
        return self.name
    