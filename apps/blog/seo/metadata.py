class SEOService:

    @staticmethod
    def get_meta(post):
        return {
            "title": post.title,
            "description": post.content[:160],
            "keywords": post.tags
        }

def post_meta(post):
    return {
        "title": post.title,
        "description": post.content[:160],
    }
