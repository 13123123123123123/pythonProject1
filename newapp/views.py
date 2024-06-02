from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'{name} {phone}\n{message}')

    return render(request, 'contact.html')
