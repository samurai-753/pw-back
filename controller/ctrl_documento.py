import random
import os
import hashlib
from app import db, UPLOAD_FOLDER
from model import Documento
from schema import SchemaDocumento
from sqlalchemy.exc import IntegrityError
from exception import ExceptionDocumentoNaoEncontrado


class CtrlDocumento:
    
    def __init__(self):
        self.schema_documento = SchemaDocumento(strict=True)
        self.schema_documentos = SchemaDocumento(strict=True, many=True)

    def calc_md5_file(self, fname):
        md5 = hashlib.md5()
        with open(fname, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()

    def add_documento(self, src_file):
        path = os.path.join(UPLOAD_FOLDER, src_file.filename)
        src_file.save(path)

        h = self.calc_md5_file(path)
        new_path = os.path.join(UPLOAD_FOLDER, h)
        os.rename(path, new_path)

        documento = Documento(src_file.filename, new_path)

        try:
            documento.idx = random.randint(0x0000, 0xffff)
            db.session.add(documento)
            db.session.commit()

            return self.dump_documento(documento)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )

    def get_documentos(self):
        documentos = Documento.query.order_by(Documento.idx).all()

        return self.dump_documentos(documentos)

    def get_documento(self, idx):
        documento = Documento.query.get(idx)

        return documento
    
    def delete_documento(self, idx):
        documento = Documento.query.get(idx)
        if not documento:
            raise Exception('idx')
            
        self.ctrl_pessoa.delete_pessoa(documento.detalhes_idx)

        db.session.delete(documento)
        db.session.commit()
    
    def update_documento(self, idx, data):
        documento = Documento.query.get(idx)
        if not documento:
            raise ExceptionDocumentoNaoEncontrado('idx', idx)

        if 'nome' in data:
            documento.nome = data['nome']

        db.session.commit()

        return self.dump_documento(documento)

    def dump_documento(self, documento):
        return self.schema_documento.dump(documento).data
    
    def dump_documentos(self, documentos):
        return self.schema_documentos.dump(documentos).data