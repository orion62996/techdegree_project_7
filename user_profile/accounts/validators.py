from django.contrib.auth import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class DifferentPasswordValidator(object):
    def validate(self, password, user=None):
        if user and user.password:
            if check_password(password, user.password):
                raise ValidationError(
                    _("The new password cannot be the same as the old password."),
                    code='must_be_different',
                )

    def get_help_text(self):
        return _(
            "The new password cannot be the same as the old password."
        )
