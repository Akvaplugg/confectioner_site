from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('catalog/', views.catalog, name='catalog'),
    path('order/', views.order_create, name='order'),
    path('api/order/', views.order_create_submit, name='order_submit'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('api/work/<int:work_id>/', views.work_detail, name='work_detail'),
]