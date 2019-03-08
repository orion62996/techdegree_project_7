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
