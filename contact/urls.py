from django.urls import path
from . import views

urlpatterns = [
    path('',views.addcontact,name="addcontact"),
    path('delete/<int:id>/', views.delete_data, name="delete_data"),
    path('<int:id>', views.updatedata, name="updatedata")
]