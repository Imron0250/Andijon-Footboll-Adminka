from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def logout_vews(request):
    logout(request)
    return redirect("login")


def index(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create_user(password=password, username=username)
        return redirect('index')
    return render(request, 'register.html')    

def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')

    return render(request, 'login.html',)


def add_player(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            second_name = request.POST.get('second_name')
            number = request.POST.get('number')
            role = request.POST.get('role')
            games_played = request.POST.get('games_played')
            minuts_played = request.POST.get('minuts_played')
            start = request.POST.get('start')
            sub_off = request.POST.get('sub_off')
            photo = request.FILES['photo']
            Player.objects.create(
                photo = photo,
                number = number,
                first_name = first_name,
                second_name = second_name,
                role = role,
                games_played = games_played,
                minuts_played = minuts_played,
                start = start,
                sub_off = sub_off,
            )
            return redirect('players_list')
        return render(request, 'add-players.html')


def edit_players(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Player.objects.get(id=pk)
            first_name = request.POST.get('first_name')
            second_name = request.POST.get('second_name')
            number = request.POST.get('number')
            role = request.POST.get('role')
            games_played = request.POST.get('games_played')
            minuts_played = request.POST.get('minuts_played')
            start = request.POST.get('start')
            sub_off = request.POST.get('sub_off')
            photo = request.FILES['photo']
            i.first_name=first_name
            i.second_name=second_name
            i.number=number
            i.role=role
            i.games_played=games_played
            i.minuts_played=minuts_played
            i.start=start
            i.sub_off=sub_off
            i.photo=photo
            i.save()
            return redirect('players_list')
        return render(request, 'edit-players.html')


def players_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
                'players': Player.objects.all().order_by('-id')
            }
        return render(request, 'players-list.html', context)

def delete_player(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Player.objects.get(id=pk).delete()
        return redirect('players_list')


def add_commant(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            logo = request.FILES['logo']
            player_id = request.POST.getlist('player')
            commant = Commant.objects.create(
                name =name,
                logo =logo,
            )
            commant.player_id.set(player_id)
            return redirect('commant_list')
        return render(request, 'add-commant.html', {'players_id':Player.objects.all()})


def edit_commant(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Commant.objects.get(id=pk)
            name = request.POST.get('name')
            logo = request.FILES['logo']
            player_id = request.POST.getlist('player')
            i.name=name
            i.logo=logo
            i.player_id.set(player_id)
            i.save()
            return redirect('commant_list')
        return render(request, 'edit-commant.html', {'players_id':Player.objects.all()})


def commant_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
                'commant': Commant.objects.all().order_by('-id')
            }
        return render(request, 'commant-list.html', context)

def delete_commant(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Commant.objects.get(id=pk).delete()
        return redirect('commant_list')


def add_Match_time(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            first_command_id = request.POST.get('first_command')
            second_command_id = request.POST.get('second_command')
            date = request.POST.get('date')
            match_time = Match_time.objects.create(
                date = date,
                first_command_id= first_command_id,
                second_command_id = second_command_id,
            )
            return redirect('match_time_list')
        else:
            return render(request, 'add-match-time.html', {'commants':Commant.objects.all()})


def edit_match_time(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Match_time.objects.get(id=pk)
            first_command_id = request.POST.get('first_command')
            second_command_id = request.POST.get('second_command')
            date = request.POST.get('date')
            i.first_command_id=first_command_id
            i.second_command_id=second_command_id
            i.date=date
            i.save()
            return redirect('match_time_list')
        return render(request, 'edit-match-time.html', {'commants':Commant.objects.all()})


def match_time_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
                'match_time': Match_time.objects.all().order_by('-id')
            }
        return render(request, 'match-time-list.html', context)

def delete_match_time(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Match_time.objects.get(id=pk).delete()
        return redirect('match_time_list')



def add_media(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            first_command_name_id = request.POST.get('first_command_name')
            second_command_name_id = request.POST.get('second_command_name')
            date = request.POST.get('date')
            photo = request.FILES['photo']
            video = request.FILES['video']
            date = request.POST.get('date')
            what_account = request.POST.get('what_account')
            media = Media.objects.create(
                date = date,
                first_command_name_id= first_command_name_id,
                second_command_name_id = second_command_name_id,
                photo = photo,
                video = video,
                what_account = what_account,
            )
            return redirect('media_list')
        else:
            return render(request, 'add-media.html', {'commants':Commant.objects.all()})


def edit_media(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Media.objects.get(id=pk)
            first_command_id = request.POST.get('first_command')
            second_command_id = request.POST.get('second_command')
            photo = request.FILES['photo']
            video = request.FILES['video']
            date = request.POST.get('date')
            what_account = request.POST.get('what_account')
            i.first_command_id=first_command_id
            i.second_command_id=second_command_id
            i.date=date
            i.photo = photo
            i.video = video
            i.what_account = what_account
            i.save()
            return redirect('media_list')
        return render(request, 'edit-media.html', {'commants':Commant.objects.all()})


def media_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
                'media': Media.objects.all().order_by('-id')
            }
        return render(request, 'media-list.html', context)

def delete_media(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Media.objects.get(id=pk).delete()
        return redirect('media_list')



def add_news(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            date = request.POST.get('date')
            title = request.POST.get('title')
            text = request.POST.get('text')
            is_banner = request.POST.get('is_banner')
            is_banner = True if is_banner == 'on' else False
            photo = request.FILES['photo']
            News.objects.create(
                date = date,
                photo = photo,
                title = title,
                text = text,
                is_banner = is_banner,
            )
            return redirect('news_list')
        else:
            return render(request, 'add-news.html')


def edit_news(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            date = request.POST.get('date')
            title = request.POST.get('title')
            text = request.POST.get('text')
            photo = request.FILES['photo']
            is_banner = request.POST.get('is_banner')
            if is_banner == 'on':
                is_banner = True
            else:
                is_banner = False
            i = News.objects.get(id=pk)
            i.photo=photo
            i.title=title
            i.text=text
            i.date=date
            i.is_banner=is_banner
            i.save()
            return redirect('news_list')
        return render(request, 'edit-news.html')


def news_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
                'news': News.objects.all().order_by('-id')
            }
        return render(request, 'news-list.html', context)

def delete_news(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        News.objects.get(id=pk).delete()
        return redirect('news_list')

def add_shop(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            product = request.POST.get('product')
            img_file = request.FILES['img_file']
            Shop.objects.create(product=product,img_file=img_file)
            return redirect('shop_list')
        return render(request, 'add-shop.html')

def edit_shop(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Shop.objects.get(id=pk)
            product = request.POST.get('product')
            img_file = request.FILES['img_file']
            i.product = product
            i.img_file = img_file
            i.save()
            return redirect('shop_list')
        return render(request, 'edit-shop.html')

def shop_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'shop' : Shop.objects.all()
        }
        return render(request, 'shop-list.html', context)

def shop_delete(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Shop.objects.get(id=pk).delete()
        return redirect('shop_list')

def add_team(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            Choose_the_form = request.POST.get('Choose_the_form')
            name = request.POST.get('name')
            Team_jersey.objects.create(Choose_the_form=Choose_the_form,name=name)
            return redirect('team_list')
        return render(request, 'add-team.html')

def edit_team(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Team_jersey.objects.get(id=pk)
            Choose_the_form = request.POST.get('Choose_the_form')
            name = request.POST.get('name')
            i.Choose_the_form=Choose_the_form
            i.name=name
            i.save()
            return redirect('team_list')
        return render(request, 'edit-team')

def team_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'team' : Team_jersey.objects.all()
        }
        return render(request, 'team-list.html', context)

def team_delete(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Team_jersey.objects.get(id=pk).delete()
        return redirect('team_list')


def add_quarter(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            quarter_number = request.POST.get('quarter_number')
            first_command_id = request.POST.get('first_command_id')
            second_command_id = request.POST.get('second_command_id')
            Quarter.objects.create(
                quarter_number = quarter_number,
                first_command_id = first_command_id,
                second_command_id =second_command_id,
            )
            return redirect('quarter_list')
        else:
            return render(request, 'add-quarter.html', {'commants':Commant.objects.all()})


def edit_quarters(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Quarter.objects.get(id=pk)
            quarter_number = request.POST.get('quarter_number')
            first_command_id = request.POST.get('first_command_id')
            second_command_id = request.POST.get('second_command_id')
            i.quarter_number=quarter_number
            i.first_command_id=first_command_id
            i.second_command_id=second_command_id
            i.save()
            return redirect('quarter_list')
        return render(request, 'edit-quarter.html', {'commants':Commant.objects.all()})

def quarter_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
                'quarter': Quarter.objects.all().order_by('-id')
            }
        return render(request, 'quarter-list.html', context)

def delete_quarter(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Quarter.objects.get(id=pk).delete()
        return redirect('quarter_list')

def add_statistic(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            match_id = request.POST.get('match_id')
            Statistic.objects.create(match_id=match_id)
            return redirect('statistic_list')
        return render(request, 'add-statistic.html', {'match_time': Match_time.objects.all()})

def edit_statistic(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Statistic.objects.get(id=pk)
            match_id = request.POST.get('match_id')
            i.match_id=match_id
            return redirect('statistic_list')
        return render(request, 'edit-statistic.html', {'match_time': Match_time.objects.all()})

def statistic_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'statistic': Statistic.objects.all()
        }
        return render(request, 'statistic-list.html', context)

def delete_statistic(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Statistic.objects.get(id=pk).delete()
        return redirect('statistic_list')



def add_about_academy(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            text = request.POST.get('text')
            photo = request.FILES['photo']
            About_academy.objects.create(photo=photo,text=text, name=name)
            return redirect('about_academy_list')
        return render(request, 'add-about-academy.html')

def edit_about_academy(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = About_academy.objects.get(id=pk)
            name = request.POST.get('name')
            text = request.POST.get('text')
            photo = request.FILES['photo']
            i.photo =photo
            i.text =text
            i.name =name
            i.save()
            return redirect('about_academy_list')
        return render(request, 'edit-about-academy.html')

def about_academy_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'about_academy' : About_academy.objects.all()
        }
        return render(request, 'about-academy-list.html', context)

def about_academy_delete(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        About_academy.objects.get(id=pk).delete()
        return redirect('about_academy_list')


def add_info(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            description = request.POST.get('description')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            logo = request.FILES['logo']
            Info.objects.create(description=description,email=email, phone=phone, logo=logo)
            return redirect('info_list')
        return render(request, 'add-info.html')

def edit_info(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Info.objects.get(id=pk)
            description = request.POST.get('description')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            logo = request.FILES['logo']
            i.description = description
            i.email = email
            i.phone = phone
            i.logo = logo
            i.save()
            return redirect('info_list')
        return render(request, 'edit-info.html',)

def info_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'info' : Info.objects.all()
        }
        return render(request, 'info-list.html', context)

def info_delete(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Info.objects.get(id=pk).delete()
        return redirect('info_list')


def add_social_media(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            logo = request.FILES['logo']
            url = request.POST.get('url')
            Social_media.objects.create(logo=logo,url=url)
            return redirect('social_media_list')
        return render(request, 'add-social-media.html')

def edit_social_media(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Social_media.objects.get(id=pk)
            logo = request.FILES['logo']
            url = request.POST.get('url')
            i.logo =logo
            i.url =url
            i.save()
            return redirect('social_media_list')
        return render(request, 'edit-social-media.html',)

def social_media_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'social_media' : Social_media.objects.all()
        }
        return render(request, 'social-media-list.html', context)

def social_media_delete(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Social_media.objects.get(id=pk).delete()
        return redirect('social_media_list')



