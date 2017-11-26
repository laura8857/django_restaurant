# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

CATEGORIES = ['日式','新疆','韓式','西式','新加坡','小吃','串燒']

def validate_category(value):
    cat = value.capitalize()
    if value not in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")
