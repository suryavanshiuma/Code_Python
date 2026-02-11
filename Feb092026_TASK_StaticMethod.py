class Facebook:
    like=0

    def ind_like(self,count):
        Facebook.like +=count
        print(count)
        
    @staticmethod
    def total_like():
        print("Total Likes: ", Facebook.like)

uma=Facebook()
uma.ind_like(6)
jay=Facebook()
jay.ind_like(7)
bhavesh=Facebook()
bhavesh.ind_like(8)

Facebook.total_like()
