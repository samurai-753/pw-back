#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AlunoDAO(object):
    instancia = None
    
    class __AlunoDAO(object):
        db_fake = []

        def add_aluno(self, aluno):
            for a in self.db_fake:
                if(a.idx == aluno.idx):
                    return False
            
            self.db_fake.append(aluno)
            return aluno.idx

        def update_aluno(self, aluno):
            edit_pos = -1
            for i in range(len(self.db_fake)):
                if aluno.idx == self.db_fake[i].idx:
                    edit_pos = i

            if(edit_pos == -1):
                return False
            
            self.db_fake[edit_pos] = aluno

            return True
    
        def delete_aluno(self, idx):
            temp = [ a for a in self.db_fake if a.idx != idx ]
            
            if(len(temp) == len(self.db_fake)):
                return False

            self.db_fake = temp
            return True

        def get_alunos(self):
            return self.db_fake

        def get_aluno(self, idx):
            for aluno in self.db_fake:
                if aluno.idx == idx:
                    return aluno
            
            return None
        


    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__AlunoDAO()

    def __getattr__(self, name):
        return getattr(self.instancia, name)