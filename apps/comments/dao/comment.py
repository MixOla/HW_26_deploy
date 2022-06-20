class Comment:
    """ Абстракция комментариев для использования в DAO """

    def __init__(self,
                 pk=0,
                 post_id=0,
                 commenter_name="",
                 comment=""
                 ):

        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

    def __repr__(self):
        return f"Post( " \
            f"{self.pk}, " \
            f"{self.post_id}, " \
            f"{self.commenter_name}, " \
            f"{self.comment}" \
            f")"

a = Comment()
print(a)