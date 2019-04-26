#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .tipo_disciplina import TipoDisciplina


class Disciplina(object):

    def __init__(self, nome, professor, tipo_disciplina=TipoDisciplina.UNDEFINED, documentos=[]):
        self.nome = nome
        self.tipo_disciplina = tipo_disciplina
        self.professor = professor
        self.documentos = documentos

    def __repr__(self):
        return '<Disciplina nome={} />'.format(self.nome)

