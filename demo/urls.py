from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', obtain_auth_token)
]
