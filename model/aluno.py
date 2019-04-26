#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self, idx, nome, email, telefone, resumo):
        super.__init__(idx, nome, email, telefone)
        
        self.resumo = resumo

    def __repr__(self):
        return '<Aluno nome={} />'.format(self.nome)