from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) # разрешение на уровне представлений
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # использование пользовательского разрешения на CRUD
    queryset = Post.objects.all()
    serializer_class = PostSerializer

