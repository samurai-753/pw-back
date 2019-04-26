#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class TipoPublicacao(Enum):
    
    UNDEFINED = 0
    CONFERENCIA = 1
    RESUMO = 2
    PERIODICO = 3