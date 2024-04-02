from django.contrib import admin    # type: ignore
from django.urls import include, path    # type: ignore

urlpatterns = [
    path('', include('blog.urls', namespace="blog")),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]
