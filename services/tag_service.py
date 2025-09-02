import uuid
from models.tag_model import Tag
from repositories.tag_repository import TagRepository
# service for Tag model
class TagService:
    @staticmethod
    def get_all_tags():
        return TagRepository.get_all()
#   get tag by id
    @staticmethod
    def get_tag(tag_id):
        return TagRepository.get_by_id(tag_id)
# create a new tag
    @staticmethod
    def create_tag(data):
        new_tag = Tag(
            id=str(uuid.uuid4()),
            name=data.get("name")
        )
        return TagRepository.create(new_tag)
# update an existing tag
    @staticmethod
    def update_tag(tag, data):
        tag.name = data.get("name", tag.name)
        TagRepository.update()
        return tag
# delete a tag
    @staticmethod
    def delete_tag(tag):
        TagRepository.delete(tag)
