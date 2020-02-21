# weeb
A simple Python program for printing out the top anime result from a search using command line arguments, using [Jikanpy](https://github.com/AWConant/jikanpy).

Prequisites
-----------
* Python
* Packages from [requirements.txt](requirements.txt)

Installing
----------
Clone the repository just about anywhere 

Example usage
-------
Make sure you have the prerequisites installed have the repository on your machine.

The program takes in the following commandline arguments
* `animetitle` - Required: Enter an anime title to search for (first argument)
* `--property` - Enter a property sort your anime result with
* `--desc` - Enter True or False for if you want the result sorted in descending order or not
* `--profilelink` - Enter a username for the program to open a browser with said profile

Example:
```
python weeb.py Naruto --property score --desc True
```

```
name: Naruto Shippuuden url: https://cdn.myanimelist.net/images/anime/5/17407.jpg?s=2bf24a22a339223dcadb1cdfc3307b61 episodes: 500 score: 8.15 synopsis: it has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now akatsuki, the myst...
```

Built with
----------
* [Jikanpy](https://github.com/AWConant/jikanpy)

Testing
-------
```
# repository root
pytest test_weeb.py
```