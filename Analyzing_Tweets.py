import string

with open('stopwords.txt','r',encoding = 'UTF-8') as stops:
    eng_words = [line.rstrip() for line in stops]

def distill_tweet(tweet):
    words = tweet.lower().replace("'",'').translate(tweet.maketrans('’-',"  ",'.,!?"')).split()
    result = []
    for word in words:
        if word not in eng_words and not word.startswith('http') and not word.isnumeric():
            result.append(word)
    return result

def tweet_lists(filename): 
    result = []
    cur_name = ''
    with open(filename, 'r') as file:
        for line in file:
            line = line.split('\t')
            user = line[1]
            tweet = line[2]
            if user == cur_name:
                cur = open(user + '.txt', 'a')
            else:
            	if cur_name != '': 
            		cur.close()
            	cur_name = user
            	result += [user]
            	cur = open(user + '.txt', 'w')
            cur.writelines(tweet + '\n')
            cur.close()
    return result 

def tweets_from_file(filename):
    with open(filename, 'r', encoding = 'UTF-8') as file:
        list_of_tweets = [line.strip() for line in file]
    return list_of_tweets

def top_entries(tweets, num_cutoff = 1, hashes = False, mentions = False):
    dict_of_tweets = {}
    list_of_tweets = []
    for item in tweets:
        fixed_tweet = distill_tweet(item)
        list_of_tweets.extend(fixed_tweet)
    if hashes:
        list_of_hashes = [word for word in list_of_tweets if word.startswith('#')]
        dict_of_tweets = {hashtag:list_of_hashes.count(hashtag) for hashtag in list_of_hashes if list_of_hashes.count(hashtag) >= num_cutoff}
    elif not hashes and mentions:
        list_of_mentions = [word for word in list_of_tweets if word.startswith('@')]
        dict_of_tweets = {users:list_of_mentions.count(users) for users in list_of_mentions if list_of_mentions.count(users) >= num_cutoff}
    else:
        list_of_words = [word for word in list_of_tweets if not word.startswith('@') and not word.startswith('#')]
        dict_of_tweets = {x:list_of_words.count(x) for x in list_of_words if list_of_words.count(x) >= num_cutoff}
    return dict_of_tweets

#Do not put your main program or any other lines of code here
