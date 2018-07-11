from django.urls import path
from .views import IndexView, add, get, update, delete

urlpatterns = [
    path('', IndexView.as_view()),
    path('get/<int:id>/', get),
    path('add-task/', add),
    path('update-task/', update),
    path('delete/<int:id>/', delete),
]
