from django import forms

from service_objects.services import Service

from core.services import ModelCreateService

from .models import Material


class BaseMaterialService(Service):
    name = forms.CharField(max_length=255)
    unit = forms.CharField(max_length=2)
    price = forms.DecimalField(decimal_places=2)
    archived = forms.BooleanField(required=False, initial=False)


class MaterialCreateService(ModelCreateService, BaseMaterialService):
    model = Material


class MaterialDestroyService:
    def __init__(self, instance):
        self.instance = instance
        self.model = instance.__class__

    def has_related(self) -> bool:
        return self.instance.uses.exists()

    def destroy(self):
        if self.has_related():
            raise Exception(
                f'Material with id {self.instance.id} cannot be deleted,'
                f' because it is used material'
            )
        self.model.objects.get(id=self.instance.id).delete()
        return self.instance.id
