-- Lists all cities from hbtn_0d_usa
SELECT cites.id, cities.name, states.name
FROM cities
JOIN states ON cites.state_id = states_id
ORDER BY cities.id;