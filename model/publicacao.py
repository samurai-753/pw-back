#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .tipo_publicacao import TipoPublicacao


class Publicacao(object):

    def __init__(self, info, documento, tipo_publicacao=TipoPublicacao.UNDEFINED):
        self.info = info
        self.documento = documento
        self.tipo_publicacao = tipo_publicacao
