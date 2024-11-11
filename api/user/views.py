from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializers import UserSerializers


class UserViewAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)


class MyProfileViewAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializers

    def get_object(self):
        return self.request.user


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializers
    queryset = User.objects.all()

    def get_object(self):
        try:
            return super(UserDetailView, self).get_object()
        except Exception as ex:
            raise ex
