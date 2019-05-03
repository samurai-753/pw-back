#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ProfessorDAO(object):
    instancia = None
    
    class __ProfessorDAO(object):
        db_fake = []

        def add_professor(self, professor):
            for p in self.db_fake:
                if(p.idx == professor.idx):
                    return False
            
            self.db_fake.append(professor)
            return professor.idx

        def update_professor(self, professor):
            edit_pos = -1
            for i in range(len(self.db_fake)):
                if professor.idx == self.db_fake[i].idx:
                    edit_pos = i

            if(edit_pos == -1):
                return False
            
            self.db_fake[edit_pos] = professor

            return True
    
        def delete_professor(self, idx):
            temp = [ p for p in self.db_fake if p.idx != idx ]
            
            if(len(temp) == len(self.db_fake)):
                return False

            self.db_fake = temp
            return True

        def get_professores(self):
            return self.db_fake

        def get_professor(self, idx):
            for professor in self.db_fake:
                if professor.idx == idx:
                    return professor
            
            return None
        


    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__ProfessorDAO()

    def __getattr__(self, name):
        return getattr(self.instancia, name)