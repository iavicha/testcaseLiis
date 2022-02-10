from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class NumAndLetterValidator:
    def __init__(self, nums=1, letters=1):
        self.nums = nums
        self.letter = letters

    def validate(self, password, user=None):
        cont_numbers = 0
        count_chairs = 0
        for i in password:
            if i in '0123456789':
                cont_numbers += 1
            elif i in 'abcdefghijklmnopqrstuvwxyz':
                count_chairs += 1
            elif i in 'abcdefghijklmnopqrstuvwxyz'.upper():
                count_chairs += 1

        if count_chairs == 0 or cont_numbers == 0:
            raise ValidationError("Пароль должен содержать хотя бы одну цифру и букву")

    def get_help_text(self):
        return _("Пароль должен содержать хотя бы одну цифру и букву")



