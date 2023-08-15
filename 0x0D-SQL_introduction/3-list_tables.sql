-- Get the database name from the argument
SET @dbname = DATABASE();

-- Show all tables in the database
SHOW TABLES FROM @dbname
