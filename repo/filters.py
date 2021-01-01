import django_filters
from .models import *
from django_filters import DateFilter

class ImageFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created",lookup_expr=)
    title_filter = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    tag_filter = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
    desc_filter = django_filters.CharFilter(field_name='description', lookup_expr='icontains')


    class Meta:
        model = Image
        fields=[]
        