"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from blog01 import views
from blog import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),
    # url(r'index/',views.index,name='index'),
    url(r'register/',views.register,name='register'),
    #media路由
    url(r'media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
    url(r'get_validCode_img/',views.get_validCode_img,name='get_validCode_img'),
    url(r'^digg/', views.digg),
    url(r'^comment/', views.comment),
    url(r'^get_comment_tree/', views.get_comment_tree),
    url(r'^upload/', views.upload),

    # 后台管理url
    url(r"cn_backend/$",views.cn_backend,name="cn_backend"),
    url(r"add_article/$",views.add_articles),
    #关于个人站点url
    url(r'^(?P<username>\w+)/$',views.home_site),
    # 个人站点的跳转
    url(r'^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$',views.home_site,name='condition'),

    url(r'^(?P<username>\w+)/articles/(?P<article_id>\d+)/$',views.article_detail,name='articles'),


    url(r'',views.index,name='index'),

]
