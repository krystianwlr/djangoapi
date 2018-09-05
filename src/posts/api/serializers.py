from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

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
	url = HyperlinkedIdentityField(
		view_name='posts-api:detail',
		lookup_field='pk'
		)

	user = SerializerMethodField()

	#delete_url = HyperlinkedIdentityField(
		#view_name='posts-api:delete',
		#lookup_field='pk'
		#)
	class Meta:
		model = Post
		fields = [
		"url",
		"id",
		"title",
		"content",
		"publish",
		"user"
		]

	def get_user(self, obj):
		return str(obj.user.username)

class PostDetailSerializer(ModelSerializer):

	user = SerializerMethodField()
	image = SerializerMethodField()
	html = SerializerMethodField()

	class Meta:
		model = Post
		fields = [
		"id",
		"title",
		"slug",
		"content",
		"html",
		"publish",
		"image",
		"user",
		]

	def get_html(self, obj):
		return obj.get_markdown()

	def get_user(self, obj):
		return str(obj.user.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None

		return image

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