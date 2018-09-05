from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		#"id",
		"title",
		#"slug",
		"content",
		"publish"
		]

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		"id",
		"title",
		"slug",
		"content",
		"publish"
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		"id",
		"title",
		"slug",
		"content",
		"publish"
		]

"""
obj = Post.objects.first()
obj_data = PostDetailSerializer(obj)
obj_data.data <- contents in json

Example for python shell:

data = {
	"title": "John Snow don't know",
	"content": "New content",
	"id": 1

}

new_item = PostDetailSerializer(data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)

obj.delete() - to remove

new_item = PostDetailSerializer(obj, data=data) - to save


"""