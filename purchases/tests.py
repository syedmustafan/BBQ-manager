import pytest
from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APITestCase
from datetime import datetime

from core.tests import BaseCRUDViewTest
from employees.models import Employee, MasterProcedure
from procedures.models import Procedure
from inventory.models import Material, MaterialUnits

from .models import UsedMaterial, Purchase, PurchaseProcedure
from .services import UsedMaterialService
from .serializers import UsedMaterialSerializer


@pytest.mark.django_db
class TestUsedMaterialService(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.model = UsedMaterial
        cls.create_service = UsedMaterialService

        cls.employee = Employee.objects.create(
            first_name='name',
            last_name='surname',
            position='someone',
            coefficient=1.11
        )
        cls.procedure_with_master = Procedure.objects.create(name='master procedure')
        cls.master_procedure = MasterProcedure.objects.create(
            procedure=cls.procedure_with_master,
            employee=cls.employee,
            price=Decimal(1),
            coefficient=0.5,
        )
        cls.purchase = Purchase.objects.create(
            time=datetime.now(),
            is_paid_by_card=False,
        )
        cls.purchase_procedure = PurchaseProcedure.objects.create(
            purchase=cls.purchase,
            procedure=cls.master_procedure
        )
        cls.material = Material.objects.create(
            name='Hair Color',
            price=Decimal('1.11'),
            unit=MaterialUnits.GRAMMS.value
        )
        cls.data = {
            'procedure': cls.purchase_procedure,
            'material': cls.material,
            'amount': 2
        }
        cls.instance = UsedMaterial.objects.create(
            procedure=cls.purchase_procedure,
            material=cls.material,
            amount=1
        )

    def test_create(self):
        count = self.model.objects.count()
        instance = self.create_service(**self.data).create()

        assert count + 1 == self.model.objects.count(), (
            f'{self.create_service.__class__.__name__} does not create instance'
        )
        assert isinstance(instance, self.model), (
            f'{self.create_service.__class__.__name__} create method does not return instance'
        )
        for k, v in self.data.items():
            assert v == getattr(instance, k)

    def test_destroy(self):
        count = self.model.objects.count()

        self.create_service(self.instance).destroy()

        assert self.model.objects.count() == count - 1, (
            f'{self.create_service.__class__.__name__} does not delete instance after destroy.'
        )


@pytest.mark.django_db
class TestUsedMaterialViews(APITestCase, BaseCRUDViewTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.serializer = UsedMaterialSerializer
        cls.model = UsedMaterial
        cls.basename = 'uses'
        cls.procedure_with_master = Procedure.objects.create(name='master procedure')
        cls.employee = Employee.objects.create(
            first_name='Max',
            last_name='Bazarov',
            position='Boss',
            coefficient=1
        )
        cls.master_procedure = MasterProcedure.objects.create(
            procedure=cls.procedure_with_master,
            employee=cls.employee,
            price=Decimal(1),
            coefficient=0.5,
        )
        cls.purchase = Purchase.objects.create(
            time=datetime.now(),
            is_paid_by_card=False,
        )
        cls.purchase_procedure = PurchaseProcedure.objects.create(
            purchase=cls.purchase,
            procedure=cls.master_procedure
        )
        cls.material = Material.objects.create(
            name='Hair Color',
            price=Decimal('1.11'),
            unit=MaterialUnits.GRAMMS.value
        )
        cls.data = {
            'procedure': cls.purchase_procedure.id,
            'material': cls.material.id,
            'amount': 2
        }
        cls.update_data = {
            'procedure': cls.purchase_procedure.id,
            'material': cls.material.id,
            'amount': 3
        }
        cls.instance = UsedMaterial.objects.create(
            procedure=cls.purchase_procedure,
            material=cls.material,
            amount=1
        )
