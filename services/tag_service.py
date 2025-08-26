import uuid
from models.tag_model import Tag
from repositories.tag_repository import TagRepository
# Tag service class
class TagService:
    @staticmethod
    def get_all_tags():
        return TagRepository.get_all()
# Get tag by id
    @staticmethod
    def get_tag(tag_id):
        return TagRepository.get_by_id(tag_id)
# Create new tag
    @staticmethod
    def create_tag(data):
        new_tag = Tag(
            id=str(uuid.uuid4()),
            name=data.get("name")
        )
        return TagRepository.create(new_tag)
# Update tag
    @staticmethod
    def update_tag(tag, data):
        tag.name = data.get("name", tag.name)
        TagRepository.update()
        return tag
# Delete tag
    @staticmethod
    def delete_tag(tag):
        TagRepository.delete(tag)
