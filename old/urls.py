from django.urls import path

from . import views

urlpatterns =[
    path(r'',views.store,name='store'),
    path('books/',views.books,name='books'),
    
    path('books/novel',views.books_novel,name='books_novel'),
    path('books/academics',views.books_academics,name='books_academics'),
    path('books/self_help',views.books_selfHelp,name='books_selfHelp'),
    path('books/updateCity',views.updateCity,name='updateCity'),
    path('update_cart/',views.updateCart,name='updateCart'),
    path('books/cart',views.cart,name='cart'),
    path('books/checkout',views.checkout,name='checkout'),
    path('accounts/login',views.login,name='login'),
    path('accounts/signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('logout1',views.logout1,name='logout1'),
    path('seller',views.seller,name='seller'),
    path('update_seller/',views.updateSeller,name='updateSeller'),
    ]