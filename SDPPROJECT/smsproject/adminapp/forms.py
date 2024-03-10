from django import forms
from .models import Faculty, Student, FacultyCourseMapping, Contact

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"password"}
        labels={"facultyid":"Enter Faculty ID","gender":"Select Gender","fullname":"Enter Full Name"}
class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"password"}
        labels={"studentid":"Enter Student ID","gender":"Select Gender","fullname":"Enter Full Name"}

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"studentid"}

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude = {"facultyid"}

class CourseMappingForm(forms.ModelForm):
    class Meta:
        model = FacultyCourseMapping
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
