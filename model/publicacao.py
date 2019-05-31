#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .tipo_publicacao import TipoPublicacao


class Publicacao(object):

    def __init__(self, idx, info, documento, tipo_publicacao=TipoPublicacao.UNDEFINED):
        self.idx = idx
        self.info = info
        self.documento = documento
        self.tipo_publicacao = tipo_publicacao
