from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count

register = template.Library()

# 最新文档
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

# 归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

# 分类
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 标签云
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)