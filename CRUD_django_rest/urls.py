from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
     # Версия апи, каждая версия предоставляет разный json, делать обновление json лучше через новую версию,
     # протестировать и сделать ее мэйном
    path('api-auth/', include('rest_framework.urls'))
]
