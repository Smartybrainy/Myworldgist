from django.urls import path
from .views import index_view, create_email_list

app_name = "core"

urlpatterns = [
    path('', index_view, name="index"),
    path('email/', create_email_list, name="email-list"),
]
