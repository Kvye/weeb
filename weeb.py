from jikanpy import Jikan
import argparse
import webbrowser
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
        anime_image = " image: " + self.specify["image_url"]
        anime_episodes = " episodes: " + str(self.specify["episodes"])
        anime_score = " score: " + str(self.specify["score"])
        anime_synopsis = " synopsis: " + self.specify["synopsis"]
        animeresult = anime_name + anime_image + anime_episodes + anime_score + anime_synopsis
        # obtain only the information we need from our search result
        return animeresult

    """returns the profile URL of the user we search for"""
    def user_profile(self, user_name):
        userprof = jikan.user(username=user_name, request='profile') # search for profile with username provided
        profileurl = userprof["url"] # take just the url
        return profileurl 
        
if __name__ == '__main__':
    """add arguments for parsing"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--animetitle", help="search for this anime") # add anime title argument
    parser.add_argument("--property", help="sort with this property") # add property argument
    parser.add_argument("--desc", default=False, help="sort by descending or not True or False") # add descending argument
    parser.add_argument("--profilelink", help="search for this users profile") # add profilelink argument
    args = parser.parse_args()

    """convert the true/false strings to booleans for the sort method"""
    boolcheck = args.desc # get our desc parameter to check if they wrote true or false
    if args.desc != False: # if the desc parameter was used
        boolcheck = args.desc.upper() # convert descending to uppercase so both True and true work etc
    if boolcheck == "TRUE": 
        args.desc = True # if user enters true the argument becomes the bool True
    elif boolcheck == "FALSE":
        args.desc = False # if user enters false the argument becomes the bool False
    q = Query(args.animetitle) # q is a search for what is entered in the animetitle parameter

    """run a sorted search if sort property is specified otherwise run a regular search"""
    if args.property == None: # if a sort property hasnt been specified
        print(q.get_anime()) # print out a search result
    else:
        print(q.sort(args.property, args.desc)) # print out a sorted search result
    
    """open a web browser with a users profile if we use the profile link param"""
    if args.profilelink: # if profilelink param is used
        webbrowser.open(q.user_profile(args.profilelink), new=2) # open web browser with profile we searched for
