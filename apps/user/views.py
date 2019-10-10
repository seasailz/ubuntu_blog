from django.shortcuts import render
from django.views import View
from django.shortcuts import render_to_response

from user.models import UserProfile
# Create your views here.


class UserInfo(View):
    def get(self, request):
        user = UserProfile.objects.all().first()
        return render(request, 'user_info.html', {
            'user': user
        })


def page_not_found(request, exception):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def pag_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
