from common.views import ViewWrapper
from projects.factories import ProductViewFactory
from django.urls import re_path

urlpatterns = [
    re_path(
        r"^projects/(?P<name>\w+)$",
        ViewWrapper.as_view(view_factory=ProductViewFactory),
    ),
]
