// Бургер-меню
document.querySelector('.burger-menu')?.addEventListener('click', function() {
    document.querySelector('.nav')?.classList.toggle('nav--active');
});

// Фильтрация портфолио
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const category = this.dataset.category;
        document.querySelectorAll('.portfolio__item').forEach(item => {
            item.style.display = category === 'all' || item.dataset.category === category ? 'block' : 'none';
        });
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});

// Маска телефона
function setPhoneMask() {
    const phoneInput = document.getElementById('id_phone');
    if (!phoneInput) return;
    
    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.startsWith('7')) value = value.substring(1);
        if (value.length > 10) value = value.slice(0, 10);
        
        let formatted = '+7 ';
        if (value.length > 0) formatted += '(' + value.substring(0, Math.min(3, value.length));
        if (value.length >= 4) formatted += ') ' + value.substring(3, 6);
        if (value.length >= 7) formatted += '-' + value.substring(6, 8);
        if (value.length >= 9) formatted += '-' + value.substring(8, 10);
        
        e.target.value = formatted;
    });
}

// Отправка формы заказа
function initOrderForm() {
    const form = document.getElementById('orderForm');
    if (!form) return;
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const name = document.getElementById('id_name')?.value.trim();
        const phone = document.getElementById('id_phone')?.value.trim();
        const orderDetails = document.getElementById('id_order_details')?.value.trim();
        const eventDate = document.getElementById('id_event_date')?.value;
        
        if (!name) {
            alert('Пожалуйста, введите ваше имя');
            return;
        }
        if (!phone || phone === '+7 ' || phone.length < 12) {
            alert('Пожалуйста, введите корректный номер телефона');
            return;
        }
        if (!orderDetails) {
            alert('Пожалуйста, опишите, что хотите заказать');
            return;
        }
        if (!eventDate) {
            alert('Пожалуйста, укажите дату события');
            return;
        }
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/api/order/', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            
            if (data.success) {
                document.getElementById('orderFormContainer').style.display = 'none';
                document.getElementById('successMessage').style.display = 'block';
            } else {
                document.getElementById('errorText').textContent = data.message;
                document.getElementById('errorMessage').style.display = 'block';
            }
        } catch (error) {
            document.getElementById('errorText').textContent = 'Ошибка соединения. Попробуйте позже.';
            document.getElementById('errorMessage').style.display = 'block';
        }
    });
}

// Запуск
document.addEventListener('DOMContentLoaded', () => {
    setPhoneMask();
    initOrderForm();
});