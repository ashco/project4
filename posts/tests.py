from django.test import TestCase
from django.urls import reverse

def create_post(post_text, days):
    """
    Create a post with the given `post_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(post_text=post_text, created_at=time)


# class PostIndexViewTests(TestCase)