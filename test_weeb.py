import pytest
from weeb import Query
query = Query("naruto") # default anime we are searching for

def test_anime_search(): # trying to test if we get the same results
    f = open("query.txt", "r")
    check = f.read()
    f.close()

    assert check == str(query.searchresults)

def test_is_sortedlist_empty(): # trying to test if the sortedlist is empty 
    emptylist = [] # our expected result

    assert query.sortedlist == emptylist

def test_specify(): # trying to test if specify is null
    assert query.specify == "null"


def test_get_anime(): # trying to test if get_anime returns the anime we search for
    f = open("naruto_get_anime.txt", "r") # our expected result
    check = f.read()
    f.close()
    
    assert check == query.get_anime()

def test_sort(): # test that sort returns the sorted result we search for
    f = open("naruto_sort.txt", "r") # our expected result
    check = f.read()
    f.close()

    assert check == query.sort()