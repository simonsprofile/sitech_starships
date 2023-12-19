from django.contrib import admin
from django.urls import path, include
from listings.urls import urlpatterns as listings
#from sales.urls import urlpatterns as sales
#from starships.urls import urlpatterns as starships


urlpatterns = [
    path('listings/', include(listings)),
    #path('sales/', include(sales)),
    #path('starships/', include(starships)),

    path('admin/', admin.site.urls),
]
