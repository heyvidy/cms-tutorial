from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_catalog),
    path('blog/<int:post_id>/', post_page),
    path('create/', create_post),
    path('signup/', signup_page),
    path('login/', signin),
    path('logout/', signout)
]
