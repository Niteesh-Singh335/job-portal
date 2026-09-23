from rest_framework.pagination import PageNumberPagination,CursorPagination

class job_list1_pagination(PageNumberPagination):
    page_size=3 
    # page_query_param='p'
    page_size_query_param='size'
    max_page_size=5
    last_page_strings='end'
class job_list1_cpagination(CursorPagination):
    page_size=3
    ordering='-date_and_time'