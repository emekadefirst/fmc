import orjson
from django.views import View
from django.http import HttpResponse

class ORJsonResponse(HttpResponse):
    def __init__(self, data, status=200, safe=True, **kwargs):
        if safe and not isinstance(data, (dict, list, tuple)):
            raise TypeError(
                "In safe mode, only dict, list, and tuple types can be serialized to JSON"
            )
        content = orjson.dumps(data)
        kwargs.setdefault("content_type", "application/json")
        super().__init__(content, status=status, **kwargs)

class AsyncView(View):
    async def get(self, request):
        return ORJsonResponse({"message": "Hello from async!"})
