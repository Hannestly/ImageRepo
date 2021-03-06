import django_filters
from .models import *
from django_filters import DateFilter
from django.db.models import Q

class ImageFilter(django_filters.FilterSet):
    title_filter = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    tag_filter = django_filters.CharFilter(field_name='tag', lookup_expr='icontains')
    desc_filter = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    combine_filter = django_filters.CharFilter(method='custom_combined_filter')

    class Meta:
        model = Image
        fields=[]

    def custom_combined_filter(self,queryset, name,value):
        return Image.objects.filter(Q(title__icontains=value) | Q(tag__icontains=value) | Q(description__icontains=value))
