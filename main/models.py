from django.db import models

class Work(models.Model):
    CATEGORY_CHOICES = [
        ('cakes', 'Торты'),
        ('cupcakes', 'Капкейки'),
        ('pastries', 'Пирожные'),
        ('desserts', 'ПП Десерты'),
    ]
    
    title = models.CharField('Название', max_length=200)
    category = models.CharField('Категория', max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField('Фото', upload_to='portfolio/')
    description = models.TextField('Описание')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cakes', 'Торты'),
        ('cupcakes', 'Капкейки'),
        ('takeaway', 'Десерты на вынос'),
    ]
    
    name = models.CharField('Название', max_length=200)
    category = models.CharField('Категория', max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    weight = models.CharField('Вес/размер', max_length=100)
    image = models.ImageField('Фото', upload_to='products/')
    description = models.TextField('Описание', blank=True)
    is_popular = models.BooleanField('Популярный', default=False)
    
    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processed', 'Обработано'),
    ]
    
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', blank=True)
    order_details = models.TextField('Что заказать')
    event_date = models.DateField('Дата события')
    reference_image = models.ImageField('Референс', upload_to='references/', blank=True, null=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата заказа', auto_now_add=True)
    
    def __str__(self):
        return f"Заказ от {self.name}"