from django.core.exceptions import PermissionDenied


class AllowParsingMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.useracc.tariff_allow_parsing:
            raise PermissionDenied

        return super(AllowParsingMixin, self).dispatch(
            request, *args, **kwargs)


class AllowPostingMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.useracc.tariff_allow_posting:
            raise PermissionDenied

        return super(AllowPostingMixin, self).dispatch(
            request, *args, **kwargs)


class AllowAnalyticsMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.useracc.tariff_allow_analytics:
            raise PermissionDenied

        return super(AllowAnalyticsMixin, self).dispatch(
            request, *args, **kwargs)
