from rest_framework import mixins, generics


class ListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Widok generyczny API zwracający listę obiektów, obsługiwana metoda GET
    """

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
