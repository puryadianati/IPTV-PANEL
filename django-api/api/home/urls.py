from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view()),
    path('user/', User.as_view(),name="user"),
    path('list/<slug:slug>/', List_Ip.as_view(),name="list_stream"),
    path('get_photo/', sex),
    path('stream/', stream2),
    path('streamhack/', stream3),   



   

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
