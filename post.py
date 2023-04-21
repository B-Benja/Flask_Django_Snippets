class Post:
    """
    Represents a blog post with an ID, title, subtitle, and body.
    """
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
