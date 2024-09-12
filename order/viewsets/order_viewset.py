

from rest_framework import viewsets


from order.models import Order
from order.serializers.order_serializers import OrderSerializer


class orderViewSet(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

   