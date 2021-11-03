from rest_framework import serializers
from .models import custom_user, info_user
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    phone = serializers.CharField(max_length=300)
    email_address = serializers.EmailField(max_length=200)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    gender = serializers.CharField(max_length=300)

    def validate_email_address(self, value):
        """
        Check that the valid email with @gmail.com is provided by the user or not in the given email.
        """
        data = self.get_initial()
        email = data.get('email_address')
        # password = value
        user_email = custom_user.objects.filter(email_address=email)

        if user_email:
            raise ValidationError("User with this email already exists.")
        return value

    # def validate_vehicle_number(self, value):
    #     data = self.get_initial()
    #     vehicle_number = data.get('vehicle_number')
    #     user_vehicle_number = custom_user.objects.filter(vehicle_number=vehicle_number)
    #
    #     if user_vehicle_number:
    #         raise ValidationError("User with this Vehicle Number already exists.")
    #     return value

    def save(self):
        account = custom_user(
            email_address=self.validated_data['email_address'],
            name=self.validated_data['name'],
            phone=self.validated_data['phone'],
            gender=self.validated_data['gender'],
            password=self.validated_data['password']
        )
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    email_address = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )


class custom_form(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    phone = serializers.CharField(max_length=300)
    email = serializers.EmailField(max_length=200,default='optional')
    language = serializers.CharField(max_length=300)
    religion = serializers.CharField(max_length=300)
    gender = serializers.CharField(max_length=300)
    location = serializers.CharField(max_length=300)
    current_city = serializers.CharField(max_length=300)
    social_media_account = serializers.CharField(max_length=300,default='optional')

    # def validate_email(self, value):
    #     data = self.get_initial()
    #     email = data.get('email')
    #     # password = value
    #     user_email = info_user.objects.filter(user__email_address=email)
    #
    #     if user_email:
    #         # raise ValidationError("Form Already Submitted")
    #         # return = "Form Already Submitted"
    #     return value

    def save(self):
        form = info_user(
            email_address=self.validated_data['email'],
            name=self.validated_data['name'],
            language=self.validated_data['language'],
            religion=self.validated_data['religion'],
            location=self.validated_data['location'],
            current_city=self.validated_data['current_city'],
            gender=self.validated_data['gender'],
            phone=self.validated_data['phone'],
            social_media_account=self.validated_data['social_media_account'],
        )
        form.save()
        return form
