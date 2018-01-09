
from django.views.generic import View,ListView
from datetime import datetime
from .models import *

from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import View, ListView
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    return render(request, 'main.html', locals())

def tickets(request):
    return render(request, 'tickets.html')

def hello(request):
    return render(request, 'hello.html')

def new(request):
    return render(request, 'new.html')


def db(request):
    return render(request, 'db.html', locals())


class HotelView(ListView):
    model = Hotel
    template_name = 'hotelsbd.html'


class CountryView(ListView):
    model = Country
    template_name = 'countrybd.html'

def hotels(request, id):
    name = ['Park_info', 'Alexandria_info', 'Voshod_info']
    Park_info = 'The Park Hotel situated in the heart of Sliema just walking distance from the Shopping Mecca and only 2 km from the UNESCO world heritage city Valletta, offers a unique location. Warmth, Style & Service are what defines Park Hotel an environment to enjoy and indulge. Bedroomed Hotel which boasts a wide selection of Room Categories, maintained to a comfortable standard set with amenities to make every stay at Park Hotel a memorable one. Our Roof Top Swimming Pool Terrace offers a relaxing area with amazing views of The Grand Harbour. Complimentary Wi-Fi is also available in Hotel Lobby & Bar area. Our hotel is the perfect option for experiencing the Maltese Islands being within easy access to Malta’s most popular Historical sites. We look forward to extending our warmest welcome to you.'
    Alexandria_info =  'До пляжа можно дойти всего за 3 минуты. Отель "Александрия" находится в 5 минутах ходьбы от берега Черного моря и располагает сауной, крытым и открытым бассейнами. К услугам гостей апартаменты с кондиционером и телевизором с плоским экраном. Все апартаменты отеля "Александрия" оформлены в красных и коричневых тонах и оснащены шкафом и кухней. В ванных комнатах установлен душ. В элегантном ресторане отеля "Александрия" подают блюда европейской и национальной украинской кухни. Для отдыха в отеле "Александрия" есть сауна и спа-салон с массажным кабинетом. Также к услугам гостей бильярд, кинотеатр, ночной клуб и конференц-зал.'
    Voshod_info = 'Отель Voshod расположен на набережной Слимы, в 3 минутах ходьбы от скалистого пляжа. Все номера оборудованы телевизором, холодильником и принадлежностями для чая/кофе. Летом на террасе подают завтрак.'
    info = [Park_info, Alexandria_info, Voshod_info]
    data1 = {'hotel': {'id': id}}
    data2 = {'hotels': [{'id': '1', 'hotel_name': 'Park Hotel', 'info': Park_info},
                       {'id': '2', 'hotel_name': 'Alexandria', 'info': Alexandria_info},
                        {'id': '3', 'hotel_name': 'Voshod', 'info': Voshod_info}]}
    return render(request, 'hotels.html', locals())

class hotelsview(View):
    def get(self, request):
        #variable = 'Django'
        today_date = datetime.now()

        data = {
            'tickets': [
                {'title': 'Первая бронь', 'id': 1},
                {'title': 'Вторая бронь', 'id': 2},
                {'title': 'Третья бронь', 'id': 3}
            ]
        }
        return render(request, 'tickets.html', locals())


class hotelview(View):
    def get(self, request, id):
        #variable = 'Django'
        today_date = datetime.now()
        data = {
            'ticket': {
                'id': id
            }
        }
        return render(request, 'ticket.html', locals())

def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success/')
        else:
            error = "Пользователь не найден"
    return render(request, 'login.html', locals())


#@login_required()
def success(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'success.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            # ...
            return HttpResponseRedirect('/login/')
        else:
            form = RegistrationForm()
    return render(request, 'registration2.html', {'form': form})
