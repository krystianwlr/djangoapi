from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		"id",
		"title",
		"slug",
		"content",
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		"id",
		"title",
		"slug",
		"content",
		]

"""
obj = Post.objects.first()
obj_data = PostSerializer(obj)
obj_data.data <- contents in json

Example for python shell:

data = {
	"title": "John Snow don't know",
	"content": "New content",
	"id": 1

}

new_item = PostSerializer(data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)

"""