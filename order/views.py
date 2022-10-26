from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Order
from .serializers import OrderSerializer

class CreateOrderView(CreateAPIView):
    serializer_class = (OrderSerializer)
    

class UserOrderList(APIView):
    
    def get(self, request):
        user = request.user
        orders = user.orders.all()
        # orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)