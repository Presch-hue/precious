`# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DoctorProfile, StudentProfile
from .models import User
from django.core.exceptions import ValidationError

class DoctorSignupForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=15)
    role = forms.CharField(max_length=35)
    email = forms.EmailField()
    profile_image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():  # Check if email already exists
            raise ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)  # Save user without committing to the database yet
        
        # Set the email for the user
        user.email = self.cleaned_data['email']
        
        if commit:
            # Save the user to the database
            user.is_doctor = True
            user.phone = self.cleaned_data['phone']
            user.save()

            # Create the DoctorProfile instance and save it
            doctor_profile = DoctorProfile(
                doctor=user,
                name=self.cleaned_data['name'],
                phone=self.cleaned_data['phone'],
                emails=self.cleaned_data['email'],
                role=self.cleaned_data['role'],
                profile_image=self.cleaned_data['profile_image']
            )
            doctor_profile.save()

        return doctor_profile  # Return the created DoctorProfile object
    
class StudentProfileForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    matric_number = forms.CharField(max_length=255, label='Matriculation Number', widget=forms.TextInput(attrs={'placeholder': 'Matriculation Number'}))
    surname = forms.CharField(max_length=255, label='Surname', widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    first_name = forms.CharField(max_length=255, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    faculty = forms.CharField(max_length=255, label='Faculty', widget=forms.TextInput(attrs={'placeholder': 'Faculty'}))
    department = forms.CharField(max_length=255, label='Department', widget=forms.TextInput(attrs={'placeholder': 'Department'}))
    level = forms.ChoiceField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')],
                              label='Level', widget=forms.Select(attrs={'placeholder': 'Select Level'}))
    profile_image = forms.ImageField(required=True, label='Profile Image', widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    # Additional validation or customization for fields can be added here if needed
    def clean_matric_number(self):
        matric_number = self.cleaned_data.get('matric_number')
        if StudentProfile.objects.filter(matric_number=matric_number).exists():
            raise ValidationError("This matric number is already in use.")
        return matric_number
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():  # Check if email already exists
            raise ValidationError("This email is already in use.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)  # Save user without committing to the database yet
        
        # Set the email for the user
        user.email = self.cleaned_data['email']
        
        if commit:
            # Save the user to the database
            user.is_student = True
            user.first_name = self.cleaned_data['first_name']
            user.surname = self.cleaned_data['surname']
            user.phone = self.cleaned_data['phone']
            user.save()

            # Create the DoctorProfile instance and save it
            student_profile = StudentProfile(
                student=user,
                matric_number=self.cleaned_data['matric_number'],
                surname=self.cleaned_data['surname'],
                first_name=self.cleaned_data['first_name'],
                faculty=self.cleaned_data['faculty'],
                department=self.cleaned_data['department'],
                level=self.cleaned_data['level'],
                profile_image=self.cleaned_data['profile_image']
            )
            student_profile.save()

        return student_profile  # Return the created StudentProfile object
