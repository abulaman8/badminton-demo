from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage


def index(request):
    return render(request, 'base/index.html')


def dashboard(request):
    return render(request, 'base/dashboard.html')


def formpage(request, action, view):
    if request.method == 'POST':
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
