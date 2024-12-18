from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# Перехватываем роуты, начинающиеся с posts/ и обрабатываем их в приложении
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace='posts'))
]

# Для отображения статики в дебаг-режиме
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
