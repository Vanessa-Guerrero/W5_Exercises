# Listing my fav movies
movies = ['Harry Potter', 'Black Panther', 'Moana', 'Frozen', 'Avatar']

print(f"The list {movies} includes my top {len(movies)} movies I'd like to watch")
print(movies)                              # 5 movies

print(sorted(movies))   # sorted alphabetically
print(movies)   # printed in same format I inserted, the sort function didn't change it

movies.sort()   # this method changed my og list and sorted it
print(movies) 

movies.append("Luck") # added the movie "Luck" as another favorite
print(movies) 