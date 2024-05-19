from django.core.exceptions import ValidationError

# my validations

def age_validator(value):
    if value < 18:
        raise ValidationError('your age has to be 18 or over.')
    return value