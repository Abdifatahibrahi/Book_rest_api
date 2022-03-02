# from django.shortcuts import render
# from django.http import JsonResponse
# from book_api.models import Book
# from book_api.serializer import BookSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serailizer = BookSerializer(books, many=True)

#     return Response(serailizer.data)

# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     if request.method == 'GET':
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
        
#     if request.method == 'PUT':
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return serializer.errors

    
#     if request.method == 'DELETE':
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return Response({
#             'delete': True
#         })



from rest_framework.views import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


    # def post(self, request):
    #     return Response({
    #         'hello': 'friend'
    #     })

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Book_detail(APIView):
    def get_book_by_pk(self, pk):
        try: 
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
