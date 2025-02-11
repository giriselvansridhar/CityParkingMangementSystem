from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Authentication/', include('Authication.urls'))  # Corrected spelling
]
