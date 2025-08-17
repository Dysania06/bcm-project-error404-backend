from models import Document, db

class DocumentController:
    @staticmethod
    def get_all():
        return Document.query.all()

    @staticmethod
    def get_by_id(document_id):
        return Document.query.get(document_id)

    @staticmethod
    def create(data):
        new_document = Document(**data)
        db.session.add(new_document)
        db.session.commit()
        return new_document

    @staticmethod
    def update(document, data):
        for key, value in data.items():
            setattr(document, key, value)
        db.session.commit()
        return document

    @staticmethod
    def delete(document):
        db.session.delete(document)
        db.session.commit()
