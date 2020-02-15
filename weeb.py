from jikanpy import Jikan
jikan = Jikan()

class Query:
    def __init__(self, name):
        pass
    def sort(self, sort_by = "score", descending = False):
        pass
    def get_anime(self, which = 0):
        pass


obtainmal = jikan.search('anime', 'Naruto') # search MAL for an anime on page 1
searchresults = obtainmal.get("results") # get only the results
sortedlist = [] # create a list for sorting
for x in searchresults:
    sortedlist.append(x["title"]) # append the sorting criteria to the sorting list
sortedlist.sort(reverse=True) # sort the list, index [0] will be considered the sorted result
for x in searchresults: # go through the search results
    if x["title"] == sortedlist[0]: # look for the result based on what is considered sorted
        specify = x # the sorted result is now our specified/final result to use
"""searches through MAL and sorts the result based on a property"""

anime_name = specify["title"] # get anime name
anime_image = specify["image_url"] # get anime image url
anime_episodes = specify["episodes"] # get anime episodes
anime_score = specify["score"] # get anime score
anime_synopsis = specify["synopsis"] # get anime synopsis
print("Name: " + anime_name,
        "Url:" + anime_image,
        "Episodes: " + str(anime_episodes), 
        "Score: " + str(anime_score), 
        "Synopsis: " + anime_synopsis
) # print name, image, episodes, score, synopsis for what we searched

obtainmal = jikan.search('anime', 'Naruto') # search MAL for an anime on page 1
searchresults = obtainmal.get("results") # get only the results
specify = searchresults[0] # take the first result only

anime_name = specify["title"] # get anime name
anime_image = specify["image_url"] # get anime image url
anime_episodes = specify["episodes"] # get anime episodes
anime_score = specify["score"] # get anime score
anime_synopsis = specify["synopsis"] # get anime synopsis
print("Name: " + anime_name,
        "Url:" + anime_image,
        "Episodes: " + str(anime_episodes), 
        "Score: " + str(anime_score), 
        "Synopsis: " + anime_synopsis
) # print name, image, episodes, score, synopsis for what we searched
"""searches through MAL for an anime and gives the title of the first result"""




if __name__ == '__main__':
    pass
