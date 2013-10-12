# -*- coding: utf-8 -*-

from django import forms
from th_rss.models import Rss


class RssForm(forms.ModelForm):

    """
        for to handle Rss service
    """

    class Meta:
        model = Rss
        fields = ('name', 'url', )


class RssProviderForm(RssForm):
    pass

