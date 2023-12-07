from django.urls import path
from django.urls import reverse_lazy

from .views import (
    DestinationListView,
    DestinationDetailView,
    DestinationUpdateView,
    DestinationDeleteView,
    DestinationCreateView,
)

urlpatterns = [
    path("<str:pk>", DestinationDetailView.as_view(), name="destination_detail"),
    path("<str:pk>/edit/", DestinationUpdateView.as_view(), name="destination_edit"),
    path(
        "<str:pk>/delete/", DestinationDeleteView.as_view(), name="destination_delete"
    ),
    path("new/", DestinationCreateView.as_view(), name="destination_new"),
    path("", DestinationListView.as_view(), name="destination_list"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
