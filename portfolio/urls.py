from django.urls import path
from .views import ProjectListView, project_list

urlpatterns = [
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('', project_list, name='project-list-view'),
]
