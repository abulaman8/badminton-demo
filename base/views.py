from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Player


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        player_type = request.POST.get('player_type')
        age = request.POST.get('age')
        dominant_hand = request.POST.get('dominant_hand')
        gender = request.POST.get('gender')
        focus = request.POST.get('focus')

        # Validation (add more as needed)
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Create the User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create the Player entry
        Player.objects.create(
            user=user,
            name=name,
            player_type=player_type,
            age=age,
            dominant_hand=dominant_hand,
            gender=gender,
            focus=focus
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'registration/signup.html')


def sigin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')


def index(request):
    return render(request, 'base/index.html')


@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html')


@login_required
def formpage(request, action, view):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if not file or file.size == 0:
            messages.error(request, "Please select a file.")
            return render(request, 'base/formpage.html')
        mc = {
            "shadow": {
                "corner": {
                    "title1": "Shadow Analysis",
                    "title2": "Minimap",
                    "vid1": staticfiles_storage.url("vid/sample.mp4"),
                    "img1": staticfiles_storage.url("img/bg.jpeg"),
                },
                "back": {
                    "title1": "Shadow Analysis",
                    "title2": "Minimap",
                    "vid1": staticfiles_storage.url("vid/sample.mp4"),
                    "img1": staticfiles_storage.url("img/bg.jpeg"),
                }
            },
            "rally": {
                "corner": {
                    "title1": "Player Analysis",
                    "title2": "Shuttle Detection",
                    "vid1": staticfiles_storage.url("vid/rally_corner_1.mp4"),
                    "vid2": staticfiles_storage.url("vid/rally_corner_2.mp4"),
                },
                "back": {
                    "title1": "Player Analysis",
                    "title2": "Shuttle Detection",
                    "vid1": staticfiles_storage.url("vid/rally_back_1.mp4"),
                    "vid2": staticfiles_storage.url("vid/rally_back_2.mp4"),
                }
            },
            "accuracy": {
                "corner": {
                    "title1": "Accuracy Analysis",
                    "vid1": staticfiles_storage.url("vid/acc_output.mp4"),
                },
                "back": {
                    "title1": "Accuracy Analysis",
                    "vid1": staticfiles_storage.url("vid/acc_output.mp4"),
                }
            }
        }
        context = {
            "vid1": mc[action][view].get("vid1"),
            "vid2": mc[action][view].get("vid2"),
            "img": mc[action][view].get("img1"),
            "title1": mc[action][view].get("title1"),
            "title2": mc[action][view].get("title2"),
            "action": action,
            "view": view
        }

        return render(request, 'base/output.html', context)
    context = {
        'action': action,
        'view': view
    }
    return render(request, 'base/formpage.html', context)


def about(request):
    return render(request, 'base/about.html')
