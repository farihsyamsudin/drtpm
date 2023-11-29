from django.contrib import admin
from django.urls import path, include
from fishtograph.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('d56b699830e77ba53855679cb1d252da/', admin.site.urls),
    path('fishtograph/', include('fishtograph.urls')),
    path('api/', include('api.urls')),
    path('loginadminnnn/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('', landing_page, name='landing_page')
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
