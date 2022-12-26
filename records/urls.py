from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.RecordListView.as_view(),
        name="record-list"
    ),
    path(
        "record/<int:pk>",
        views.RecordDetailView.as_view(),
        name="record-detail"
    ),
    path(
        "create",
        views.RecordCreateView.as_view(),
        name="record-create"
    ),
    path(
        "record/<int:pk>/update",
        views.RecordUpdateView.as_view(),
        name="record-update",
    ),
    path(
        "record/<int:pk>/delete",
        views.RecordDeleteView.as_view(),
        name="record-delete",
    ),
]