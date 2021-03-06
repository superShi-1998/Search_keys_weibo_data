"""weibo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from weibo_app import weibo_search,save_json_img,down_data
from weibo_app import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^weibo_keys/keys/(\S+)/pageNum/(\d+)/$', weibo_search.weibo_keys),
    url(r'^img/keys/(\S+)/pageNum/(\d+)/$',save_json_img.Down_img),
    # url(r'^down_data/keys/(\S+)/pageNum/(\d+)/$', down_data.down_data)
]
