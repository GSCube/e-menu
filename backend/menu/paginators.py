from rest_framework.pagination import PageNumberPagination


class MenuPaginator(PageNumberPagination):
    page_size = 15
