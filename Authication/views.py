from django.shortcuts import render, redirect
from django.http import HttpResponse
from Authication import otp  # Ensure this module has correct OTP generation & sending logic


def Login(request):
    if request.method == "POST":
        Number = request.POST.get('Number')
        if Number:
            return redirect(f"OTP/?phoneno={Number}")  # Redirect to OTP page
        else:
            return HttpResponse("Invalid phone number")

    return render(request, 'Loginpage.html')


def OTP(request):
    OTPa = None  # Store generated OTP
    Number = request.GET.get('phoneno')
    
    if not Number:
        return HttpResponse("Invalid request, phone number missing.")
    
    Number = "+91" + Number  # Format phone number
    
    if request.method == "POST":
        # Collect OTP entered by user
        OTP = "".join([
            request.POST.get(f'otp{i}', '') for i in range(1, 7)
        ])
        print(f"User entered OTP: {OTP}")

        # Retrieve OTP from session storage
        OTPa = request.session.get('generated_otp')
        
        if OTP == OTPa:
            return HttpResponse("OTP Verified Successfully!")
        else:
            return HttpResponse("Invalid OTP. Please try again.")

    # Generate a new OTP and store it in the session
    OTPa = otp.generate_otp()
    request.session['generated_otp'] = OTPa  # Store OTP for verification
    otp.send_otp_via_whatsapp(Number, OTPa)  # Send OTP via WhatsApp

    context = {"Phoneno": Number}
    return render(request, 'OTP.html', context=context)
