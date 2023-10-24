-- Create user_0d_1 and set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVLIGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVLIGES;