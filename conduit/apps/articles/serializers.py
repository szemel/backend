from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'author',
            'body',
        )

    def get_author(self, obj):
        return obj.author.username


class CreateCommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'body',
        )


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    description = serializers.CharField(required=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'author',
            'body',
            'createdAt',
            'description',
            'comments',
            'title',
            'image',
        )

    def get_created_at(self, instance):
        return instance.created_at.isoformat()


