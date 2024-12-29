CREATE USER IF NOT EXISTS 'task_tracker'@'localhost' IDENTIFIED  BY 'task_tracker';
CREATE DATABASE IF NOT EXISTS task_tracker;
GRANT ALL PRIVILEGES ON task_tracker.* TO 'task_tracker'@'localhost';
FLUSH PRIVILEGES;