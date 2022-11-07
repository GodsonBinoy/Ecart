
from django.urls import path
from . import views
app_name='ecartapp'

urlpatterns = [
    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='procatdetail'),

]
