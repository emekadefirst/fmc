from asgiref.sync import sync_to_async
from user.backend import CustomBackend

@sync_to_async
def get_queryset(model):
    return list(model.objects.all())

@sync_to_async
def get_object(model, pk):
    return model.objects.get(pk=pk)

@sync_to_async
def save_object(serializer):
    return serializer.save()

@sync_to_async
def delete_instance(instance):
    instance.delete()

@sync_to_async
def validate_serializer(serializer):
    return serializer.is_valid()

@sync_to_async
def login_user(request, user):
     CustomBackend.authenticate(request, user)




