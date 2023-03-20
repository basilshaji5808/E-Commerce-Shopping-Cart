from django.urls import path

from . import views
app_name = 'onlineshopingapp'
urlpatterns = [

    path('',views.allProdcat,name='allProdcat'),
    path('<slug:c_slug>/', views.allProdcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.ProductDetails, name='products_details'),

]