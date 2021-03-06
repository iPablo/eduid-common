# -*- coding: utf-8 -*-

from eduid_common.api.utils import get_flux_type

__author__ = 'lundberg'


class FluxResponseStatus(object):

    @property
    def ok(self):
        return 'ok'

    @property
    def error(self):
        return 'error'


class FluxResponse(object):

    def __init__(self, req, suffix, payload, error=None, meta=None):
        self.flux_type = get_flux_type(req, suffix)
        self.payload = payload
        self.meta = meta
        self.error = error

    def __repr__(self):
        return u'<{!s} ({!r})>'.format(self.__class__.__name__, self.to_dict())

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return u'{!s} ({!r})'.format(self.__class__.__name__, self.to_dict())

    def to_dict(self):
        rv = dict()
        rv['type'] = self.flux_type
        if self.payload:
            rv['payload'] = self.payload
        if self.error:
            rv['error'] = self.error
        if self.meta:
            rv['meta'] = self.meta
        return rv


class FluxSuccessResponse(FluxResponse):

    def __init__(self, req, payload, meta=None):
        FluxResponse.__init__(self, req, 'success', payload, meta=meta)


class FluxFailResponse(FluxResponse):
    def __init__(self, req, payload, meta=None):
        FluxResponse.__init__(self, req, 'fail', payload, error=True, meta=meta)
