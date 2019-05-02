#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from .pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self, idx, nome, email, telefone, resumo):
        super().__init__(idx, nome, email, telefone)
        
        self.resumo = resumo

    def set_from_dict(self, data):
        self.nome = data['nome']
        self.email = data['email']
        self.telefone = data['telefone']
        self.resumo = data['resumo']

    @staticmethod
    def from_dict(data):
        idx = random.randrange(0x0000, 0xffff)
        p = Aluno(idx, data['nome'], data['email'], data['telefone'], data['resumo'])
        return p

    def __repr__(self):
        return '<Aluno idx={} nome={} />'.format(self.idx, self.nome)