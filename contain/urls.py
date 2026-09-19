from django.urls import path
from .import views


from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('',views.Home, name="home"),
    path("login/",views.Login,name="login"),
    path("signup/",views.Signup,name="register"),
    path('category/living_room/', views.Living, name="living"),
    path('category/dining_room/', views.Dining, name="dining"),
    path('category/bed_room/', views.Bed, name="bed"),
    path('category/home_office/', views.Office, name="office"),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)