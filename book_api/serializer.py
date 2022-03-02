from rest_framework import serializers
from book_api.models import Book
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    n_o_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()


    def create(self, data):
        return Book.objects.create(**data)