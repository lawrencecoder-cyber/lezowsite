class UserAdapter:
    """
    Central place for transforming user-related data.
    Useful for APIs and external integrations.
    """

    @staticmethod
    def to_dict(user):
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "bio": user.bio,
        }
