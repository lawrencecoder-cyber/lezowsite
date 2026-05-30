class SchemaService:

    @staticmethod
    def article_schema(post):
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": post.title,
            "articleBody": post.content,
            "datePublished": str(post.created_at),
            "author": post.author.username
        }
