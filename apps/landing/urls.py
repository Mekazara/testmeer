from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.landing.views import IndexPageView

app_name = 'landing'

urlpatterns =[
    path('', IndexPageView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)