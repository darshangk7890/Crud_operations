from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.BlogListCreate.as_view(), name="blog-view-create"),
    path("blog/<int:pk>/", views.BlogRetriveUpdateDestroy.as_view(), name="update"),
]