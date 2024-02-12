from ..models.restaurant import Restaurant


def shop_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'shop_detail.html', {'restaurant': restaurant})