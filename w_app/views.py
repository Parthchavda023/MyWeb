from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.mail import send_mail
from NotesWeb import settings
from .forms import *
import random


# Create your views here.
otp = 0         
def index(request):
    msg = ''
    user = request.session.get('user')
    if request.method == 'POST':
        # Signup
        if request.POST.get('signup') == 'signup':
            newdata = signupForm(request.POST)
            if newdata.is_valid():
                # Unique username
                username=newdata.cleaned_data.get('username')   # Unique username
                try:
                    signupModel.objects.get(username=username)  # Unique username
                    print("Username is already exists!")
                    msg="Username is already exists!"
                except signupModel.DoesNotExist:
                    newdata.save()
                    print("Signup Successfully!")
                    msg="Signup Successfully!"

                    # OTP sending
                    global otp
                    otp = random.randint(1111,9999)
                    print('Your OTP is- ',otp)
                    sub = 'OTP varification'
                    mssg = f"Your OTP is -: {otp}"
                    from_id = settings.EMAIL_HOST_USER
                    to_id = [request.POST['username']]
                    send_mail(subject=sub, message=mssg, from_email=from_id, recipient_list=to_id)
                    return redirect('otpverify')
            else:
                print(newdata.errors)
                msg = 'Something Went wrong! Try again...!'
        # Login
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            user = signupModel.objects.filter(username=unm, password=pas)
            uid = signupModel.objects.get(username=unm)     # Update
            if user: #True
                print('Login Successfully..!')
                msg = 'Login Successfully..!'
                request.session['user'] = unm
                request.session['userid'] = uid.id  # Update
                return redirect('notes')
            else:
                print('Please check Your Username & Password. Try again...!')
                msg = 'Please check Your Username & Password. Try again...!'
                
    return render(request, 'index.html', {'msg':msg, 'user':user})

def notes(request):
    msg = ''
    user = request.session.get('user')
    if request.method == 'POST':
        # Signup
        if request.POST.get('signup') == 'signup':
            newdata = signupForm(request.POST)
            if newdata.is_valid():
                # Unique username
                username=newdata.cleaned_data.get('username')   # Unique username
                try:
                    signupModel.objects.get(username=username)  # Unique username
                    print("Username is already exists!")
                    msg="Username is already exists!"
                except signupModel.DoesNotExist:
                    newdata.save()
                    print("Signup Successfully!")
                    msg="Signup Successfully!"
            else:
                print(newdata.errors)
                msg = 'Something Went wrong! Try again...!'
        # Login
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            user = signupModel.objects.filter(username=unm, password=pas)
            uid = signupModel.objects.get(username=unm)     # Update
            if user: #True
                print('Login Successfully..!')
                msg = 'Login Successfully..!'
                request.session['user'] = unm
                request.session['userid'] = uid.id  # Update
                return redirect('notes')
            else:
                print('Please check Your Username & Password. Try again...!')
                msg = 'Please check Your Username & Password. Try again...!'
    
        # Notes Form
        elif request.POST.get('notesform') == 'notesform':
            if request.method == 'POST':
                notesdata = notesForm(request.POST, request.FILES)
                if notesdata.is_valid():
                    notesdata.save()
                    print("Notes sent Successfully.")
                    msg = "Sent Successfully...!"
                else:
                    print(notesdata.errors)
                    msg = 'Something went wrong, try again...!'
                
    return render(request, 'notes.html', {'msg':msg, 'user':user})

def about(request):
    return render(request, 'about.html')

def contact(request):
    msg =''
    if request.method == 'POST':
        feedbackdata = feedbackForm(request.POST)
        if feedbackdata.is_valid():
            feedbackdata.save()
            print('Feedback send Successfully.')
            msg = 'Feedback send Successfully.'

            # Send Email
            sub = request.POST['subject']
            mssg = f"Hello Dear, {request.POST['name']}\n\nThanks for send your feedback...!\nWe will connect shortly.\n\nThank & Regards.\nTeam NotesApp,\n+91 932855315+ | notesapp@gmail.com | www.NotesApp.com"
            from_id = settings.EMAIL_HOST_USER
            to_id = [request.POST['email']]
            send_mail(subject=sub, message=mssg, from_email=from_id, recipient_list=to_id)

        else:
            print(feedbackdata.errors)
            msg = 'Somthing went wrong, Try again...!'

    return render(request, 'contact.html', {'msg':msg})

def profile_update(request):
    msg = ''
    user = request.session.get('user')  # Show username    
    userid = request.session.get('userid')
    uid = signupModel.objects.get(id=userid)
    if request.method == 'POST':
        updatedata = updateForm(request.POST, instance=uid)
        if updatedata.is_valid():
            updatedata.save()
            print('Data updated Successfully')
            msg = 'Profile updated Successfully...!'
        else:
            print(updatedata.errors)
    return render(request, 'profile.html', {'user':user, 'uid':uid, 'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('/')

def otpverify(request):
    global otp
    msg = ''
    if request.method == "POST":
        if request.POST['otp'] == str(otp):
            print("OTP Verify successfully!")
            msg="OTP Verify successfully!"
            return redirect('/')
        else:
            msg="Verification faild...Try again!"

    return render(request, 'otpverify.html', {'msg':msg})


