from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  

class SignUpForm(UserCreationForm):  

    def saveButDontActivate(self):
        user = self.save(commit=False)  
        user.is_active = False  
        user.save() 
        return user

    def sendActivationEmail(self, request, user):
        current_site = get_current_site(request) 
        mail_subject = 'Activate your account.'  
        message = render_to_string('students/acc_active_email.html', {  
            'user': user,  
            'domain': current_site.domain,  
            'uid':  urlsafe_base64_encode(force_bytes(user.pk)),  
            'token': account_activation_token.make_token(user),  
        })  
        to_email = self.cleaned_data.get('email')  
        email = EmailMessage( mail_subject, message, to=[to_email] )  
        email.send()

    class Meta:  
        model = User  
        fields = ('email', 'first_name', 'last_name', 'username')