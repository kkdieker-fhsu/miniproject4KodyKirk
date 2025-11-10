from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#custom form for making the login page look better
class CustomAuthenticationForm(AuthenticationForm):
    #this runs when the form is called
    def __init__(self, *args, **kwargs):
        #run the original init
        super().__init__(*args, **kwargs)

        #add form-control to the username and password fields
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )

#similar story here, adding form control to the base form for styling purposes
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'}
            )
