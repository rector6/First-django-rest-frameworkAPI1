from django.urls import path
from . import views
 


urlpatterns = [
    path('Category',views.CategoryList.as_view()),
    path('Category/<int:id>',views.CategoryDetail.as_view()),
    path('Books',views.BookList.as_view()),
    path('Books/<int:id>',views.BookDetail.as_view()),
    path('products',views.productsList.as_view()),
    path('products/<int:id>',views.productsDetail.as_view()),
]