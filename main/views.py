from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings
from .models import Work, Product, Order
import requests

def index(request):
    return render(request, 'main/index.html')

def portfolio(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        works = Work.objects.all()
    else:
        works = Work.objects.filter(category=category)
    return render(request, 'main/portfolio.html', {
        'works': works,
        'categories': Work.CATEGORY_CHOICES,
    })

def work_detail(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    return JsonResponse({
        'id': work.id,
        'title': work.title,
        'image_url': work.image.url,
        'description': work.description,
    })

def catalog(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=category)
    return render(request, 'main/catalog.html', {
        'products': products,
        'categories': Product.CATEGORY_CHOICES,
    })

@csrf_exempt
@require_http_methods(['POST'])
def order_create_submit(request):
    try:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email', '')
        order_details = request.POST.get('order_details')
        event_date = request.POST.get('event_date')
        
        if not name or not phone or not order_details or not event_date:
            return JsonResponse({'success': False, 'message': 'Заполните все поля'})
        
        order = Order.objects.create(
            name=name, phone=phone, email=email,
            order_details=order_details, event_date=event_date,
            reference_image=request.FILES.get('reference_image')
        )
        
        message = f"""
🆕 НОВЫЙ ЗАКАЗ #{order.id}

👤 Имя: {name}
📞 Телефон: {phone}
📧 Email: {email or 'не указан'}

🍰 Заказ: {order_details}

📅 Дата: {event_date}
"""
        # Отправка на почту
        try:
            send_mail(
                subject=f'Новый заказ #{order.id} от {name}',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONFECTIONER_EMAIL],
                fail_silently=False
            )
        except:
            pass
        
        return JsonResponse({'success': True, 'message': 'Заказ принят! Я свяжусь с вами'})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

def order_create(request):
    return render(request, 'main/order.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')