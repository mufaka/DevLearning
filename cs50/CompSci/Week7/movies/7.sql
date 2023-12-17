SELECT m.title, r.rating FROM movies m JOIN ratings r on r.movie_id = m.id WHERE m.year = 2010 ORDER BY r.rating DESC, m.title ASC;