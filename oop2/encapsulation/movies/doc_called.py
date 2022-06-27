from documentary import Documentary
m = Documentary()
m._add_movie('My octopus teacher',2020,'Documentary')
m.add_channel('Netflix')
m._get_movie()

#access protected attribute from super class (movie)
print(f'Title : {m._title}')