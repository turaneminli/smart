from django.urls import path
from .views import BulbList, UsersList
from .views import MultiTen


urlpatterns = [
    path('users/', UsersList.as_view(), name='users_list'),

    # This is just an example. DELETE it when starting a new project!
    path('add/', MultiTen.as_view(), name='testinc_celery'),
    path('', BulbList.as_view(), name='bulblist'),
]