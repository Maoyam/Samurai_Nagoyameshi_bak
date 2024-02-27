from django.shortcuts import render, get_object_or_404
from django.views import View
from commondb.models.restaurant import Restaurant
from commondb.models.area import Area
from commondb.models.genre import Genre

class SearchView(View):
    def get(self, request):
        keyword = request.GET.get('search')
        
        restaurants = Restaurant.objects.filter(name__icontains=keyword)  # キーワードに一致する店舗を検索
        return render(request, 'shop_list_search.html', {'restaurants': restaurants})

class GenreFilterView(View):
    def get(self, request, genre):
        restaurants = Restaurant.objects.filter(genre=genre)  # ジャンルに一致する店舗を検索
        return render(request, 'general/shop_list_filter.html', {'restaurants': restaurants})

class AreaFilterView(View):
    def get(self, request, area):

        restaurants = Restaurant.objects.filter(area=area)  # エリアに一致する店舗を検索
        return render(request, 'general/shop_list_filter.html', {'restaurants': restaurants})
