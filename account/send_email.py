from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Hello! Activate your account!',
        f'To activate your account you need to link: {full_link}',
        'abdb2226@gmail.com',
        [user],
        fail_silently=False
    )


def send_notification(user, order_id, total_price):
    email = user.email
    send_mail(
        'Уведомление о создании заказа',
        f'Вы создали заказ {order_id},\Стоимость заказа: {total_price}\nОжидайте звонка!\nСпасибо за покупку',
        'abdb2226@gmail.com',
        [email],
        fail_silently=False
    )

def send_code_password_reset(user):
    code = user.activation_code 
    email = user.email
    send_mail(
        'Письмо с кодом для сброса пароля!',
        f'Ваш код для востановления: {code}',
        'abdb2226@gmail.com',
        [user],
        fail_silently=False
    )