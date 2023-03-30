from multiprocessing import context
from django.shortcuts import redirect , render
from django.contrib.auth import logout,authenticate,login
# from django.shortcuts import HttpResponse

from django.contrib import messages
# from pkg_resources import require
from .models import *

# Create your views here.
default_data = {}



def signin(request):
    if request.method == "POST":
        Email = request.POST['Email']
        password = request.POST['password']



        # User_login = authenticate(Email=email , Passsword = password)

        # if User_login is not None:
        #     login(request, User_login)
        #     return redirect('profile')

        # else:
        #     # ----------------- return redirect('register')
        #     messages.success(request, 'Incorrect Password')
        # #     # print('incorrect password')

        try:
            user = User_login.objects.get(Email = Email)
            if user.Password == password:
                request.session['Email'] = Email        #session creation
                return redirect('profile')
            else:
                messages.success(request, 'Incorrect Password')
                # print('incorrect password')

        except User_login.DoesNotExist as err:
            print('record not found!', err)
    
    # return redirect(login)
    return render(request,'login.html')

# def admin_login(request): 
#     return render(request,'admin_login')

def register(request):
    if request.method == "POST":
        Name= request.POST['name']
        Email = request.POST['Email']
        Password = request.POST['password']
        # print(Name,Email,Password)
        data = User_login.objects.create(Name=Name, Email=Email, Password = Password)
        User_data.objects.create(User_login=data)
        messages.success(request, 'Your account Successfully create Now you can logedIn.')
        return redirect('signin')
        # if len(Name)<2:
        #         messages.success(request, 'Your account not  Successfully create.')
        # else:
        #     data = User_login.objects.create(Name=Name, Email=Email, Password = Password)
        #     User_data.objects.create(User_login=data)
        #     messages.success(request, 'Your account   Successfully create.')
    return render(request,'register.html')

def add_detail(request):
    # context = {'success' : False}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['phone']
        work = request.POST['occupation']
        print(name,email,number,work)
        data2=occupation.objects.create(name=name,email=email,number=number,work=work)
        # context = {'success' : True }
        data2.save()
    return render(request,'add_detail.html')

def see_detail(request):
    all_data = occupation.objects.all()
    # print(all_data)
    context = {'see_detail' : all_data }
    return render(request,'see_detail.html',context)

def see_message(request):
    all_data = Notification.objects.all()
    # print(all_data)
    context = {'see_message' : all_data }
    return render (request,'notification.html',context)


def message(request):
    if request.method == "POST":
        title = request.POST['title']
        Message= request.POST['message']
        date = request.POST['date']
        # print(Message)
        data=Notification.objects.create(date=date,title=title,Message=Message)
        data.save()
        # Notification.objects.create(Message=data1)
        # messages.success(request, 'Message Sent Successfully')
        
    return render(request, 'message.html')

def profile_data_load(request):
    r_user = User_login.objects.get(Email = request.session['Email'])
    profile_data = User_data.objects.get(User_login = r_user)
    default_data['profile_data'] = profile_data

def profile_update(request): 
    if request.method == "POST":
        r_user = User_login.objects.get(Email = request.session['Email'])
        profile_data = User_data.objects.get(User_login = r_user)

        profile_data.First_name = request.POST['first_name']
        profile_data.Last_name = request.POST['last_name']
        profile_data.Email_Address = request.POST['Email']
        # profile_data.country = request.POST['country']
        profile_data.House_No = request.POST['house_no']
        # profile_data.dob = request.POST['dob']
        profile_data.Mobile_No = request.POST['phone']
        # profile_data.Gender = request.POST['gender']
        profile_data.Occupation = request.POST['occupation']
        # profile_data.member = request.POST['member']
        profile_data.Alternate_No = request.POST['alternate_contact_no']
        profile_data.total_Vehicles = request.POST['total_vehicle']
        # profile_data.profile_image = request.FILES['profile_image']
        

        profile_data.save()
     
        return redirect('profile')

def profile(request):  
    profile_data_load(request)
    return render(request,'profile.html',default_data)

def contact(request):
    return render(request,'contact.html')

def add_image(request):
    return render(request,'add_image.html')

def see_image(request):
    return render(request,'see_image.html')

def admin_page(request):
    return render(request,'admin.html')

def upload_image(request):
    if request.method == "POST":
        image = request.FILES ['image']

        image_add.objects.create(image=image)

        return redirect('image_fetch')

def image_fetch(request):
    all_img = image_add.objects.all()
    return render(request,'see_image.html',{'key1' : all_img})

        



def admin_login(request):
    return render(request,'admin_login.html')

# def register_fun(request):
#     messages.success(request, 'Your account Successfully create.')
#     if request.method == "POST":
#         Name= request.POST['name']
#         Email = request.POST['email']
#         Password = request.POST['password']
#         data = User_login.objects.create(Name=Name, Email=Email, Password = Password)
#         User_data.objects.create(User_login=data)
#     return render(request,'register.html')


# def login_fun(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User_login.objects.get(Email = email)
#             if user.Password == password:
#                 request.session['email'] = email        #session creation
#                 return redirect(profile)
#             else:
#                 messages.success(request, 'Incorrect Password')
#                 # print('incorrect password')

#         except User_login.DoesNotExist as err:
#             print('record not found!', err)
    
#     return redirect(login)

def logout_user(request):
    logout(request)
    messages.success(request, 'You Logout Successfully.')
    return redirect('signin')

# def logout_user(request):
#     if 'email' in request.session:
#         del request.session['email']
#     return redirect(login)    













