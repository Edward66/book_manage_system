from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from book_manage_system import settings


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = settings.WHITE_LIST

        if request.path in white_list:
            return None
        else:
            if not request.user.is_authenticated:
                return redirect('/login/')
