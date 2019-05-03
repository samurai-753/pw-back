#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from .pessoa import Pessoa


class Professor(Pessoa):
    
    def __init__(self, idx, nome, email, telefone, sala, titulos):
        super().__init__(idx, nome, email, telefone)

        self.sala = sala
        self.titulos = titulos

    def set_from_dict(self, data):
        self.nome = data['nome']
        self.email = data['email']
        self.telefone = data['telefone']
        self.sala = data['sala']
        self.titulos = data['titulos']

    @staticmethod
    def from_dict(data):
        idx = random.randrange(0x0000, 0xffff)
        p = Professor(
            idx, data['nome'], data['email'],
            data['telefone'], data['sala'], data['titulos']
        )

        return p

    def __repr__(self):
        return '<Professor idx={} nome={} />'.format(self.idx, self.nome)

    def __eq__(self, professor):
        for key, value in self.__dict__.items():
            if(professor.__dict__[key] != value):
                return False

        return True