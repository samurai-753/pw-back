import schema
import model
import app
from pprint import pprint


if __name__ == "__main__":
    pess = model.Pessoa(idx=0x1234, nome='KatoMono123', email='kato@samurai.io2', telefone='') 
    prof = model.Professor(detalhes_idx=1642, sala='dcc2')
    prof.detalhes = pess

    s_pessoa = schema.SchemaPessoa()
    s_professor = schema.SchemaProfessor()

    print(s_pessoa.dumps(pess).data)
    print(s_professor.dumps(prof).data)