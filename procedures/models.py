from django.db import models


class Procedure(models.Model):

    class Meta:
        db_table = 'precedures'

    name = models.CharField('Procedure_name', max_length=255)

    def __str__(self) -> str:
        return self.name
