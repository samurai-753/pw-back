import json
import random

class Professor:

    def __init__(self, idx, nome, email, telefone, sala, titulos):
        self.idx = idx
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.sala = sala
        self.titulos = titulos
    
    def set_senha(self, senha):
        self.senha = senha

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
        p.set_senha(data['senha'])

        return p
    
    def __repr__(self):
        return '<Professor idx={} nome={} />'.format(self.idx, self.nome)