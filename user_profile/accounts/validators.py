from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class DifferentPasswordValidator(object):
    def validate(self, password, user=None):
        if check_password(password, user.password):
            raise ValidationError(
                _("You must enter a password that is different from your current password."),
                code='must_be_different',
            )

    def get_help_text(self):
        return _(
            "Your new password cannot be the same as the old password."
        )


class UppercaseLowercaseValidator(object):
    def validate(self, password, user=None):
        has_upper = False
        has_lower = False
        for character in password:
            if character.isupper():
                has_upper = True
            if character.islower():
                has_lower = True
        if not has_upper or not has_lower:
            raise ValidationError(
                _("Your password must contain uppercase and lowercase letters."),
                code='must_contain_upper_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain uppercase and lowercase letters."
        )


class ContainsNumericDigit(object):
    def validate(self, password, user=None):
        has_digit = False
        for character in password:
            if character in "1234567890":
                has_digit = True
        if not has_digit:
            raise ValidationError(
                _("Your password must contain at lease one numeric digit."),
                code='must_contain_digit',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one numeric digit."
        )


class ContainsSpecialCharacter(object):
    def validate(self, password, user=None):
        has_special_character = False
        for character in password:
            if character in "!\"#$%&*'()+,./-":
                has_special_character = True
        if not has_special_character:
            raise ValidationError(
                _("Your password must contain at lease one special character."),
                code='must_contain_special_character',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one special character."
        )
