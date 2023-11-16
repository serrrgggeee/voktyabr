from django import forms


__all__ = ['BootstrapCharInput', 'BootstrapPasswordInput', 'BootstrapTextarea',
           'BootstrapSelect', 'BootstrapDateTimeInput']


class BootstrapControlMixin(object):
    """
    Mixin, который из простых html-виджетов, делает Bootstrap input'ы.

    Достаточно всего лишь добавить класс 'form-control'.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control'


class BootstrapCharInput(BootstrapControlMixin, forms.TextInput):
    pass


class BootstrapPasswordInput(BootstrapControlMixin, forms.PasswordInput):
    pass


class BootstrapTextarea(BootstrapControlMixin, forms.Textarea):
    pass


class BootstrapSelect(BootstrapControlMixin, forms.Select):
    pass


class BootstrapDateTimeInput(BootstrapControlMixin, forms.DateTimeInput):
    pass