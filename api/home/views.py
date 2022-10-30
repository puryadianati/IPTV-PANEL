from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404,reverse


# Create your views here.
def Home(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    return render(request, "index.html", context)


class User(TemplateView):
    template_name = "user.html"


class List_Ip(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import requests
        name = self.kwargs.get('slug')
        list_url = []
        name_list = []
        provider = []
        ses = requests.Session()
        ses.headers['User-Agent'] = 'Mozilla/5'
        url = "http://195.201.0.157:25500/login.php"
        ref = "http://195.201.0.157:25500/login.php"
        headers = {"Referer": ref}
        password = {'username': 'admin', 'password': 'admin'}
        cookiename = ''
        cookievalue = ''
        response = ses.post(url, data=password, headers=headers)
        cookieJar = ses.cookies
        for cookie in cookieJar:
            cookiename = cookie.name
            cookievalue = cookie.value

        x = requests.get('http://195.201.0.157:25500/api.php?action=stream&sub=list&catstream=' + name + '&pageno=1',
                         cookies={'PHPSESSID': cookievalue})
        import json

        # JSON string

        # Convert string to Python dict
        from urllib.parse import urlparse
        employee_dict = json.loads(x.text)
        for i in range(0, len(employee_dict['data']['items'])):
            list_url.append(
                employee_dict['data']['items'][i]['id']['stream_source'].replace("\\", "").replace('"', '').replace('[',
                                                                                                                    '').replace(
                    ']', ''))

            provider.append(urlparse(
                employee_dict['data']['items'][i]['id']['stream_source'].replace("\\", "").replace('"', '').replace('[',
                                                                                                                    '').replace(
                    ']', '')).netloc)
            name_list.append(employee_dict['data']['items'][i]['id']['stream_display_name'])
            import itertools
            all = zip(list_url, name_list, provider)

        context['url'] = all
        context['name'] = name_list
        return HttpResponse(employee_dict)


def sex(request):
    slug = request.GET['name']
    import cv2
    vidcap = cv2.VideoCapture(
        slug)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("media_cdn/frame%d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `width`
        height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(height)
        from PIL import ImageFont, ImageDraw, Image
        import numpy as np
        import cv2

        import cv2

        image = cv2.imread(r"C:\Users\purya\Desktop\django-api\api\media_cdn\frame%d.jpg" % count, 1)

        font = cv2.FONT_HERSHEY_COMPLEX
        x, y, w, h = 0, 0, 175, 75

        cv2.putText(image, str(height) + ' p', (0, 150), font, 5, (0, 0, 255),
                    5)  # text,coordinate,font,size of text,color,thickness of font
        cv2.imwrite("media_cdn/frame%d.jpg" % count, image)

        return redirect("http://127.0.0.1:8000/media/frame0.jpg")


def stream(requets):
    import requests
    file_name = str(0) + ".ts"
    link = 'http://venomtt.com:8000/50643437655519/30565206953908/190949'
    print("Downloading file:%s" % file_name)

    # create response object
    r = requests.get(link, stream=True)
    # download started
    with open("media_cdn/" + file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
    return HttpResponse("ok")


def stream2(request):
    import os
    import requests
    from django.http import StreamingHttpResponse
    url = 'https://lb.vhls.ru.com/cdn/premium61/tracks-v1a1/2022/08/01/21/39/17-08340.ts'
    filename = os.path.basename(url)
    r = requests.get(url, stream=True)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Disposition'] = f'attachement; filename="porya.ts"'
    return response


def stream3(request):
    import os
    import requests
    from django.http import StreamingHttpResponse
    url = 'http://primetv.site:8080/test-reseller-1e73c0/4661/196435'
    filename = os.path.basename(url)
    r = requests.get(url, stream=True)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Disposition'] = f'attachement; filename="sex.ts"'
    return response


from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('must_authenticate')
        return render(request, 'chart.html')


####################################################

## if you don't want to user rest_framework

# def get_data(request, *args, **kwargs):
#
# data ={
#             "sales" : 100,
#             "person": 10000,
#     }
#
# return JsonResponse(data) # http response


#######################################################

## using rest_framework classes

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    redirect_authenticated_user = True

    def get(self, request, format=None):


        labels = [
            'cpu ( % ) ',
            'ram ( % ) ',

        ]

        import requests
        name = ""
        list_url = []
        name_list = []
        provider = []
        ses = requests.Session()
        ses.headers['User-Agent'] = 'Mozilla/5'
        url = "http://195.201.0.157:25500/login.php"
        ref = "http://195.201.0.157:25500/login.php"
        headers = {"Referer": ref}
        password = {'username': 'admin', 'password': 'admin'}
        cookiename = ''
        cookievalue = ''
        response = ses.post(url, data=password, headers=headers)
        cookieJar = ses.cookies
        for cookie in cookieJar:
            cookiename = cookie.name
            cookievalue = cookie.value

        x = requests.get('http://195.201.0.157:25500/api.php?action=stats', cookies={'PHPSESSID': cookievalue})
        import json

        # JSON string

        # Convert string to Python dict
        from urllib.parse import urlparse
        employee_dict = json.loads(x.text)

        chartLabel = "Main server"
        chartdata = [employee_dict['servers'][0]['cpu'], employee_dict['servers'][0]['mem']]
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
            "uptime": employee_dict['servers'][0]['uptime'],
            "input": employee_dict['servers'][0]['bytes_received'],
            "output": employee_dict['servers'][0]['bytes_sent'],
            "input1": employee_dict['servers'][0]['total_streams'],
            "input2": employee_dict['servers'][0]['total_running_streams'],
            "input3": employee_dict['servers'][0]['total_connections'],

        }
        return Response(data)
