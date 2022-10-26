from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class Mark:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    marks = (
        (one, 'Too bad'),
        (two, 'bad'),
        (three, 'normal'),
        (four, 'good'),
        (five, 'excellent'),
    )

class Review(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    owner = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=Mark.marks)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.product}: {self.rating} rate -> {self.text}'