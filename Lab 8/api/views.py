from django.http import JsonResponse
from django.views import View
from .models import Product, Category


class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values(
            'id', 'name', 'price', 'description',
            'count', 'is_active', 'category_id'
        ))
        return JsonResponse(products, safe=False)


class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.values(
                'id', 'name', 'price', 'description',
                'count', 'is_active', 'category_id'
            ).get(pk=id)
            return JsonResponse(product)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)


class CategoryListView(View):
    def get(self, request):
        categories = list(Category.objects.values('id', 'name'))
        return JsonResponse(categories, safe=False)


class CategoryDetailView(View):
    def get(self, request, id):
        try:
            category = Category.objects.values('id', 'name').get(pk=id)
            return JsonResponse(category)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)


class CategoryProductsView(View):
    def get(self, request, id):
        products = list(Product.objects.filter(category_id=id).values(
            'id', 'name', 'price', 'description',
            'count', 'is_active', 'category_id'
        ))
        return JsonResponse(products, safe=False)