-- Lists all cities from hbtn_0d_usa
SELECT cites.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cites.state_id = states.id
ORDER BY id ASC;