from models.document_model import Document, db
#  document repository
class DocumentRepository:
    @staticmethod
    def get_all():
        return Document.query.all()
# get document by id
    @staticmethod
    def get_by_id(document_id):
        return Document.query.get(document_id)
# create document
    @staticmethod
    def create(document):
        db.session.add(document)
        db.session.commit()
        return document
# update document
    @staticmethod
    def update():
        db.session.commit()
# delete document
    @staticmethod
    def delete(document):
        db.session.delete(document)
        db.session.commit()
