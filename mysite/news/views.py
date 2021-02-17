from django.http import HttpResponse


# Create your views here.
def mainpage(request):
    return HttpResponse('Main Page!')

def index(request):  # request - объект с данными о запросе, клиенте, куки, данные сессий и т.д.
    # все что можно увидеть в консоли веб-разработчика
    # В ответ на запрос надо что-то вернуть, какой-то ответ
    return HttpResponse('<h1>Hello World!</h1>')


def test(request):
    return HttpResponse('<h1>Test page</h1>')
