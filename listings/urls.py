from django.urls import path

from .views import (
    ListingsList,
    ListingsDetail,
    #SalesList,
    #SalesDetail,
)


urlpatterns = [
    path('', ListingsList.as_view(), name='Listings'),
    path('<int:id>/', ListingsDetail.as_view(), name='Listing Detail'),
    #path('', SalesList.as_view(), name='Sales List'),
    #path('<int:id>/', SalesDetail.as_view(), name='Sales Detail'),
]
