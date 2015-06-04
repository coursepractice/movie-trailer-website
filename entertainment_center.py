import media
import fresh_tomatoes
#the first movie, internship.
movie1 = media.Movie("Internship",
                     "an interesting movie",
                     "http://www.openlettersmonthly.com/issue/wp-content/uploads/2013/06/banner1.jpg",
                     "https://www.youtube.com/watch?v=NyfSMnMBGiM")
#the second movie, kingsman secret service
movie2 = media.Movie("Kingsman",
                     "another interesting movie",
                     "http://i.ytimg.com/vi/un-U2mmznVI/maxresdefault.jpg",
                     "https://www.youtube.com/watch?v=kl8F-8tR8to")
#compose the movies into an array to be iterable so that can be used by fresh_tomatoes
movies = [movie1, movie2]

fresh_tomatoes.open_movies_page(movies)
