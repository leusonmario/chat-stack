class Comment:

    def __init__(self, comment):
        self.id = comment[0]
        self.associated_post = comment[1]
        self.score = comment[2]
        self.text = comment[3]
        self.creation = comment[4]
        self.user_id = comment[6]