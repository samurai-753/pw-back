#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .publicacao import Publicacao


class Documento(Publicacao):
    
    def __init__(self, nome, path):
        self.nome = nome
        self.path = path

    def __repr__(self):
        return '<Documento nome={} />'.format(self.nome)