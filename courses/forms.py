from django import forms

class EnrollmentForm(forms.Form):
    course_name = forms.CharField(widget=forms.HiddenInput())
    student_name = forms.CharField(max_length=100, label="Full Name")
    student_email = forms.EmailField(label="Email Address")
    student_phone = forms.CharField(max_length=15, label="Phone Number")

    def clean_student_phone(self):
        phone = self.cleaned_data['student_phone']
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone
