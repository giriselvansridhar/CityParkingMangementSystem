from django.shortcuts import render, redirect
from django.http import HttpResponse


def Login(request):
    if request.method == "POST":
        Signup=None
        Number = request.POST.get('Number')
        Signup=request.POST.get('sup')



        if Number:
            return redirect(f"OTP/?phoneno={Number}")  # Redirect to OTP page

        
        if Signup:
            return redirect('SignUp')
        
        
        


    return render(request, 'Loginpage.html')


def OTP(request):
    
    return render(request, 'PIN.html')

def SignUp(request):
    return render(request, 'signup.html')