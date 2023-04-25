from django.urls import path
from .views import home, book_detail, book_create, read
from django.conf import settings
from django.conf.urls.static import static
# app_name = "courses"

urlpatterns = [
    path("", home, name="home"),
    path("books/create", book_create, name="book-create"),
    path("books/<int:pk>/", book_detail, name="book-detail"),
    path("read/book/<int:pk>/", read, name="read-book"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)