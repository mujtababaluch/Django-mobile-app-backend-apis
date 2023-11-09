from django.shortcuts import render
from rest_framework import generics
from .models import Categories, User, products
from .serializers import  ProductsSerializer, ProductsearchSerializer, UserSerializer
from rest_framework import filters,status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse,HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout as django_logout



class ProductsList(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):     
        category_name = self.kwargs['category_name']  # Retrieve the category name from the URL parameter
        category = get_object_or_404(Categories, Category_name=category_name)
        return products.objects.filter(Category_name=category)
    



def search_products(request):
    query = request.GET.get('query')
    if query:
        product_results = products.objects.filter(
            Q(product_name__icontains=query) | Q(product_desc__icontains=query)
        )
        results = []
        for product in product_results:
            product_data = {
                'product_name': product.product_name,
                'product_desc': product.product_desc,
                'price': product.price,
                'color': product.color,
                'size_one': product.size_one.name,
                'size_two': product.size_two.name if product.size_two else None,
                'size_three': product.size_three.name if product.size_three else None,
                'size_four': product.size_four.name if product.size_four else None,
            }
            # Add image URLs to the product data
            product_data['product_picone'] = product.product_picone.url if product.product_picone else None
            product_data['product_pictwo'] = product.product_pictwo.url if product.product_pictwo else None
            product_data['product_picthree'] = product.product_picthree.url if product.product_picthree else None
            product_data['product_picfour'] = product.product_picfour.url if product.product_picfour else None
            results.append(product_data)
        
        return JsonResponse({'results': results})
    else:
        return JsonResponse({'error': 'No search query provided.'})
    
# users/views.py


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

    if not user.check_password(password):
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Login successful'})
@api_view(['POST'])
def logout(request: HttpRequest):
    django_logout(request)
    return Response({'message': 'Logout successful'})