from django.contrib import admin

from .models import Department, Material, Purpose, Order, Course, Order_material

# Register your models here.
admin.site.register(Department)
admin.site.register(Material)
admin.site.register(Purpose)
admin.site.register(Order)
admin.site.register(Course)
admin.site.register(Order_material)
