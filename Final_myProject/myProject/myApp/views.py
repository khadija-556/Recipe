from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import login,logout,authenticate
from myApp.models import *
from .forms import *
import random
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import get_user_model
from myApp.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from myProject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

def singupPage(request):
    if request.method == 'POST':
        form=customUserForm(request.POST)
        if form.is_valid():
            # user=form.save(commit=False)
            # user.is_active=False
            # user.save()
            # activateEmail(request, user, form.cleaned_data.get('email'))
            # messages.success(request, 'Registration successful. You are now logged in.')
           
            
            form.save()
            return redirect('singinPage')
    else:
        form=customUserForm()
    return render(request,"singupPage.html",{'form':form})


def singinPage(request):
    if request.method == 'POST':
        form=CustomerAutenticationForm(request,data=request.POST)
        if form.is_valid():
           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            
            user=authenticate(username =username,password = password)
            login(request,user)
            return redirect("homePage")
    else:
            form=CustomerAutenticationForm()

    return render(request,"singin.html",{'form':form})

def activate(request,uid64,token):
    User=get_user_model()
    try:
        uid= force_str(urlsafe_base64_decode(uid64))
        user=User.objects.get(pk=uid)

    except:
        user =None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('singinPage')

    print("account activation: ", account_activation_token.check_token(user, token))

    return redirect('singinPage')


def activateEmail(request,user,to_mail):
    mail_sub='Active your user Account'
    message=render_to_string("template_activate.html",{
        'user': user.username,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        'protocol':'https' if request.is_secure() else 'http'
    })
    email= EmailMessage(mail_sub, message, to=[to_mail])
    if email.send():
        messages.success(request,f'Dear')
    else:
        message.error(request,f'not')


def logoutPage(request):
    logout(request)

    return redirect("singinPage")


def forget_pass(request):
    if request.method == 'POST':
        my_email=request.POST.get('email')
        user=Custom_User.objects.get(email=my_email)
        otp=random.randint(111111,999999)
        user.otp_token=otp
        user.save()

        sub=f"""Your OTP is {otp}"""
        msg=f"""Your OTP is {otp}.Don't share it"""
        form_mail=EMAIL_HOST_USER
        receipent =[my_email]

        send_mail(
            subject=sub,
            message=msg,
            from_email=form_mail,
            recipient_list=receipent,
        )

        return redirect("update_pass")
    return render(request,'forget_pass.html')

def update_pass(request):
    if request.method == 'POST':
        mail=request.POST.get("email")
        otp=request.POST.get("otp")
        password=request.POST.get("password")
        c_password=request.POST.get("c_password")

        user = Custom_User.objects.get(email=mail)

        if user.otp_token != otp:
            return redirect("forget_pass")
        
        if password != c_password:
            return redirect("forget_pass")
        
        user.set_password(password)
        user.otp_token =None
        user.save()
        return redirect("singinPage")
    return render(request,'update_pass.html')


def homePage(request):
    return render(request,"homePage.html")

def Recipi_catagories(request):
    if request.method == "POST":
        form=Recipi_catagoriesForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect("viewRecipi")
    else:
        form=Recipi_catagoriesForm()
    
    return render(request,'Recipi_catagories.html',{'form':form})

def Recipi(request):
    if request.method == "POST":
        form=RecipiForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect("viewRecipi")
    else:
        form=RecipiForm()
    
    return render(request,'Recipis.html',{'form':form})

def viewRecipi(request):
    task=RecipiModel.objects.all()
  
    return render(request,"viewRecipi.html",{'task':task,})
  

def search_results(request):
    query = request.GET.get('query')
    
    recipes = RecipiModel.objects.filter(
        Q(RecipiTitle__icontains=query) |
        Q(tags__icontains=query) 
       
    ).distinct()

    return render(request, 'search_results.html', {'recipes': recipes, 'query': query})

def add_to_favorites(request, recipe_id):
    recipe = RecipiModel.objects.get(pk=recipe_id)
    favorite_recipe, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)

    if created:
        pass
    else:
        pass

    return redirect('viewRecipi')


def editRecipi(request, id):
    obj=RecipiModel.objects.get(id=id)
    if request.method == 'POST':
        form = RecipiForm(request.POST, instance=obj) 
        if form.is_valid():
            form.save()
            return redirect("viewRecipi")

    else:
        form = RecipiForm(instance=obj) 

    return render(request, 'EditRecipi.html', {'form': form})



def RecipiDeletePage(request, id):
    RecipiModel.objects.filter(id=id).delete()
    
    messages.success(request, 'Recipi Delete Successfully!')

    return redirect('viewRecipi')

