from rest_framework import serializers
from book_api.models import Book
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     n_o_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()


#     def create(self, data):
#         return Book.objects.create(**data)

#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.n_o_pages = data.get('n_o_pages', instance.n_o_pages)
#         instance.publish_date = data.get('publish_date', instance.publish_date)
#         instance.quantity = data.get('quantity', instance.quantity)
        
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
