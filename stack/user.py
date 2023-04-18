class User:

    def __init__(self, user):
        try:
            self.id = user['user_id']
            self.id = user['user_id']
            self.reputation = user['reputation']
            self.profile_link = user['link']
            try:
                self.acceptance_rate = user['accept_rate']
            except:
                print("User has no acceptance rate")
                self.acceptance_rate = None
        except:
            print("Annonymous question.")
            self.id = 'anon'
            self.id = None
            self.reputation = None
            self.profile_link = None
            self.acceptance_rate = None