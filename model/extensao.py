#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .tipo_extensao import TipoExtensao


class Extensao(object):

    def __init__(self, inicio, fim, documento, tipo_extensao=TipoExtensao.UNDEFINED):
        self.inicio = inicio
        self.fim = fim
        self.tipo_extensao = tipo_extensao
        self.documento = documento

    def __repr__(self):
        return '<Extensao inicio={} fim={} />'.format(self.inicio, self.fim)

