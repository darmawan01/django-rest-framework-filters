
from rest_framework import pagination, viewsets

from rest_framework_filters import backends

from .filters import DFUserFilter, NoteFilterWithRelatedAll, UserFilterWithAll
from .models import Note, User
from .serializers import NoteSerializer, UserSerializer


class DFUserViewSet(viewsets.ModelViewSet):
    # used to test compatibility with the drf-filters backend
    # with standard django-filter FilterSets.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = DFUserFilter


class FilterFieldsUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (backends.DjangoFilterBackend, )
    filter_fields = {
        'username': '__all__',
    }


class ComplexFilterFieldsUserViewSet(FilterFieldsUserViewSet):
    queryset = User.objects.order_by('pk')
    filter_backends = (backends.ComplexFilterBackend, )
    filter_fields = {
        'id': '__all__',
        'username': '__all__',
        'email': '__all__',
    }

    class pagination_class(pagination.PageNumberPagination):
        page_size_query_param = 'page_size'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = UserFilterWithAll


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = NoteFilterWithRelatedAll
