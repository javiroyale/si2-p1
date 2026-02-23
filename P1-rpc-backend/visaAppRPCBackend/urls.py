from django.urls import path
from modernrpc.views import RPCEntryPoint

urlpatterns = [
    path("rpc/", RPCEntryPoint.as_view(), name="rpc")
]



