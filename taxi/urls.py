from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    CarCreateView,
    CarUpdateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    CarDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("Manufacturer/create", ManufacturerCreateView.as_view(), name="Manufacturer-list-create"),
    path("car/create", CarCreateView.as_view(), name="Car-list-create"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="Car-list-update"),
    path("Manufacturer/<int:pk>/update/", ManufacturerUpdateView.as_view(), name="Manufacturer-list-update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="Car-list-delete"),
    path("Manufacturer/<int:pk>/delete/", ManufacturerDeleteView.as_view(), name="Manufacturer-list-delete")
]

app_name = "taxi"
