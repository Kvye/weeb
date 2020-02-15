from jikanpy import Jikan
jikan = Jikan()

class Query:
    """Searches for the anime being queried"""
    def __init__(self, name):
        anime = jikan.search('anime', name) # searches for anime with the name provided
        self.searchresults = anime.get("results") # get the results only
        self.sortedlist = [] # empty list to be used for sorting
        self.specify = "null" # string to be used for our final specified result

    """Sorts and returns our anime search results based on a property and in descending order or not"""
    def sort(self, sort_by = "score", descending = False):
        for x in self.searchresults: # go through all the results
            self.sortedlist.append(x[sort_by]) # append to a list every instance of the property we are using
        self.sortedlist.sort(reverse=descending) # sort that list to sort our results
        for x in self.searchresults: # go through all the results again
            if x[sort_by] == self.sortedlist[0]: # if current index is same as our sorted list
                self.specify = x # then that index is the sorted result we want
                anime_name = "name: " + self.specify["title"] 
                anime_image = "image: " + self.specify["image_url"]
                anime_episodes = "episodes: " + str(self.specify["episodes"])
                anime_score = "score: " + str(self.specify["score"])
                anime_synopsis = "synopsis: " + self.specify["synopsis"]
                animeresult = anime_name + anime_image + anime_episodes + anime_score + anime_synopsis
                # obtain only the information we need from our sorted search result
                return animeresult                

    """Returns our top/first anime result or one we specify with an index"""
    def get_anime(self, which = 0):
        self.specify = self.searchresults[which] # obtain the search result index
        anime_name = "name: " + self.specify["title"]
        anime_image = "image: " + self.specify["image_url"]
        anime_episodes = "episodes: " + str(self.specify["episodes"])
        anime_score = "score: " + str(self.specify["score"])
        anime_synopsis = "synopsis: " + self.specify["synopsis"]
        animeresult = anime_name + anime_image + anime_episodes + anime_score + anime_synopsis
        # obtain only the information we need from our search result
        return animeresult

q = Query("Naruto") # q is a search for "Naruto" 
print(q.sort()) # print out a sorted search result
print(q.get_anime()) # print out a search result

if __name__ == '__main__':
    pass
