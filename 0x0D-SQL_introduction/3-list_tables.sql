-- Connect to the database passed as argument
USE $1;

-- Query the information_schema.tables view to get the table names
SELECT table_name
FROM information_schema.tables
WHERE table_schema = '$1';
