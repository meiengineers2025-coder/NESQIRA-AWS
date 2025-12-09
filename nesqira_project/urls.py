from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line routes requests starting with 'ltv/' to our app's URL file
    path('ltv/', include('ltv_tracker.urls')), 
]
