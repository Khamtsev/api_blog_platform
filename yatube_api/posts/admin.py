from django.contrib import admin

from .models import Post, Comment, Group, Follow


class PostAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_display = ('id', 'author', 'text', 'group',
                    'pub_date', 'image', )
    list_display_links = ('group', )
    list_editable = ('text',)
    list_filter = ('author', 'group', 'pub_date')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_display = ('id', 'author', 'text', 'post',
                    'created', )
    list_display_links = ('post', )
    list_editable = ('text',)
    list_filter = ('author', 'post', 'created', )


class GroupAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('id', 'title', 'slug', 'description', )
    list_editable = ('description',)


class FollowAdmin(admin.ModelAdmin):
    search_fields = ('user', )
    list_display = ('id', 'user', 'following', )
    list_display_links = ('user', 'following', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
