from django.forms import ModelForm
from .models import AddBook,SignUp,SignIn

class AddBookForm(ModelForm):
    class Meta:
        model=AddBook
        fields='__all__'

class SignUpForm(ModelForm):
    class Meta:
        model=SignUp
        fields='__all__'

class SignInForm(ModelForm):
    class Meta:
        model=SignIn
        fields='__all__'

