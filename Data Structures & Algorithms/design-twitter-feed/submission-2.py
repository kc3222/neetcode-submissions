class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # userId: (count, tweetId)
        self.followMap = defaultdict(set) # userId: followeeIds
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if self.tweetMap[userId] == 10:
            self.tweetMap[userId].pop(0)
        self.tweetMap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            allTweets.extend(self.tweetMap[followeeId])
        allTweets = sorted(allTweets, key = lambda x: x[0], reverse=True)
        allTweets = [allTweets[i][1] for i in range(min(len(allTweets), 10))]
        return allTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)
