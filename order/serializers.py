from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields= ('product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(write_only=True, many=True)
    status = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        fields= '__all__'

    def create(self, validated_data):
        products = validated_data.pop('products')
        request = self.context['request']
        user = request.user
        order = Order.objects.create(user=user, status='open')
        for product in products:
            try:
                OrderItem.objects.create(order=order,
                                            product=product['product'],
                                            quantity=product['quantity'],)
            except KeyError:
                OrderItem.objects.create(order=order,
                                            product=product['product'],)
        return order
        
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['products'] = OrderItemSerializer(instance.items.all(), many=True).data
        repr.pop('product')
        products = OrderItem.objects.filter(order=instance)
        total_price = 0
        total_price += [item.quantity * item.product.price for item in products]
        [print(x.product, x.product.title, x.product.price, x.quantity, '\n'+'='*100) for x in products]
        
        return repr