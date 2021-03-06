# coding:utf-8

from django.urls import re_path
from common import api as capi
from .asset_permission import asset_permission_urlpatterns
from .application_permission import application_permission_urlpatterns

from .remote_app_permission import remote_app_permission_urlpatterns
from .database_app_permission import database_app_permission_urlpatterns
from .system_user_permission import system_users_permission_urlpatterns
from .k8s_app_permission import k8s_app_permission_urlpatterns

app_name = 'perms'

old_version_urlpatterns = [
    re_path('(?P<resource>user|user-group|asset-permission|remote-app-permission)/.*', capi.redirect_plural_name_api)
]

urlpatterns = asset_permission_urlpatterns + \
              application_permission_urlpatterns + \
              remote_app_permission_urlpatterns + \
              database_app_permission_urlpatterns + \
              k8s_app_permission_urlpatterns + \
              old_version_urlpatterns + \
              system_users_permission_urlpatterns
