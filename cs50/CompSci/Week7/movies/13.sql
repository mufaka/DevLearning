WITH actor AS (SELECT id as actor_id FROM people WHERE name = 'Kevin Bacon' and birth = 1958)
SELECT name 
FROM people, actor
WHERE id 
IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT movie_id FROM stars WHERE person_id = actor.actor_id))
AND id <> actor.actor_id;
