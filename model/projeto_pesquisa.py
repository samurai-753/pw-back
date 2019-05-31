#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ProjetoPesquisa(object):

    def __init__(self, idx, nome, orientador, alunos=[],  coorientador=None):
        self.idx = idx
        self.nome = nome
        self.orientador = orientador
        self.coorientador = coorientador
        self.alunos = alunos
    
    def __repr__(self):
        s = '{} '.format(self.coorientador) if self.coorientador else ''
        
        return '<ProjeotPesquisa nome={} orientador={} {}/>'.format(
            self.nome, self.orientador, s
        )

