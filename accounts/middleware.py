from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout


class PrintHello(MiddlewareMixin):
    def process_request(self,request):
        user = request.user
        if not user.is_active:
            logout(request)

            # return redirect("check_active")
