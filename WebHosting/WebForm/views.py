from django.shortcuts import render, HttpResponseRedirect, HttpResponse

from .models import registrationForm

from .forms import formView,formSign

def hosting(request):
    return render(request,'hosting.html')

def webHost(request):
    return render(request,'WebHostingHome.html')

def myformview(request):
    if request.method == 'POST':
        form = formView(request.POST)
        if form.is_valid() and "Register" in request.POST:
            f = form.save(commit=False)
            f.save()

        signup = formSign()
        context = {
            's': signup,
        }
        return render(request, 'sign.html', context )

    else:
        form = formView()
        context = {
            'form': form
        }
        return render(request,'register.html', context)

# def savesignup(request):
#     if request.method == 'POST':
#         form = formSign(request.POST)
#         if form.is_valid() and "SignUp" in request.POST:
#             f = form.save(commit=False)
#             f.save()
#             context = {'f': f}
#     return render(request, 'WebHostingHome.html',context)


def mySignUp(request):
    if request.method == 'POST':
        form=formSign(request.POST)
        if form.is_valid and "SignUp" in request.POST:
            f=form.save(commit=False)
            f.save()
            context={'f':f}
        return render(request, 'WebHostingHome.html', context)

    else:
        if request.method == 'GET':
            s = formSign()
        context = {
            's': s
        }
        return render(request,'sign.html', context)
