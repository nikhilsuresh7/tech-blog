from django.urls import path

from .views import (
    blog_post_list_view,
    blog_post_create_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
    )

urlpatterns = [
    path('', blog_post_list_view),
    path('create-new/', blog_post_create_view),
    path('<int:id>/', blog_post_detail_view),
    path('<int:id>/edit/', blog_post_update_view),
    path('<int:id>/delete/', blog_post_delete_view),

]
