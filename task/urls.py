from django.urls import path
from . import views
from .views import TaskViews, TaskDetails, TaskNew

urlpatterns = [
        path('', TaskViews.as_view(), name='task_list'),
        path('task/<int:pk>', TaskDetails.as_view(), name='task_details'),
        path('taskNew/', TaskNew.as_view(), name='task_new'),
]