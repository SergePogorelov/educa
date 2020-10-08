from rest_framework import serializers

from ..models import Subject, Course, Module, User, Content


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "title", "slug"]


class ModuleSerializer(serializers.ModelSerializer):

    course = serializers.StringRelatedField()

    class Meta:
        model = Module
        fields = ["order", "title", "description", "course"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class CourseSerializer(serializers.ModelSerializer):

    modules = ModuleSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "title",
            "slug",
            "overviev",
            "created",
            "owner",
            "modules",
            "students",
        ]


class ItemReletedFields(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):

    item = ItemReletedFields(read_only=True)

    class Meta:
        model = Content
        fields = ["order", "item"]


class ModuleWithContentsSerializer(serializers.ModelSerializer):

    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ["order", "title", "description", "contents"]


class CourseWithContentsSerializer(serializers.ModelSerializer):

    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "title",
            "slug",
            "overviev",
            "created",
            "owner",
            "modules",
            "students",
        ]
