#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ProfessorDAO(object):
    instancia = None
    
    class __ProfessorDAO(object):
        db_fake = []

        def add_professor(self, professor):
            self.db_fake.append(professor)

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
            self.db_fake = [ p for p in self.db_fake if p.idx != idx ]
            
            return True

        def get_professors(self):
            return self.db_fake

        def get_professor(self, idx):
            for professor in self.db_fake:
                if professor.idx == idx:
                    return professor
        


    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__ProfessorDAO()