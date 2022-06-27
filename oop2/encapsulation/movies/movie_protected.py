class Movie:
    def __init__(self) -> None:
        #protected attribute
        self._title_ = ''
        self._year_ = 0
        self._genre = ''
        self._rating = 6

    #protected method begin with _
    def _add_movie(self,title,year,genre,rating = 6):
        self._title = title
        self._year = year
        self._genre = genre
        self._rating = rating

    def _get_movie(self):
        print(f'title : {self._title}\nyear : {self._year}\nraiting : {self._rating}')