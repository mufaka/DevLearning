WITH film AS (select id as movie_id from movies WHERE title = 'Toy Story')
SELECT p.name FROM stars s, film JOIN people p ON p.id = s.person_id WHERE s.movie_id = film.movie_id 
