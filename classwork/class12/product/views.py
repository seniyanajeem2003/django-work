from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK



@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def product_list(request):
    products = [
        {"name": "Chips", "price": 50, "category": "Snacks"},
        {"name": "Face Serum", "price": 300, "category": "Cosmetics"},
        {"name": "Chair", "price": 200, "category": "Furniture"},
        {"name": "T-Shirt", "price": 400, "category": "Clothing"},
        {"name": "Book", "price": 300, "category": "Education"},
    ]
    return Response(products, status=HTTP_200_OK)
