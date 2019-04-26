#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Pessoa(object):
    
    def __init__(self, idx, nome, email, telefone):
        self.idx = idx
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Pessoa nome={} />'.format(self.nome)