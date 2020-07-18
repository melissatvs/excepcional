from drf_yasg.inspectors import CoreAPICompatInspector, NotHandled
from rest_framework import filters


class DjangoFilterDescriptionInspector(CoreAPICompatInspector):

    def get_filter_parameters(self, filter_backend):

        if isinstance(filter_backend, filters.DjangoFilterBackend):
            result = super(DjangoFilterDescriptionInspector,
                           self).get_filter_parameters(filter_backend)

            for param in result:
                if not param.get('description', ''):
                    param.description = \
                        "Filter the returned list by {field_name}".format(
                            field_name=param.name)

            return result

        return NotHandled


class EventOrderingFilter(filters.OrderingFilter):
    ordering_description = "Ordenação por: Data/Hora, Nível"
