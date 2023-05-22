from django.test import TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(name="Menu1", price=10, inventory=30)
        Menu.objects.create(name="Menu2", price=20, inventory=40)
        Menu.objects.create(name="Menu3", price=10, inventory=50)
        
    def test_getall(self):
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)
        
        
        