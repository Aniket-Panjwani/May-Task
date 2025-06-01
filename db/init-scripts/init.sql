-- ============================================================================
-- File: db/init-scripts/init.sql
-- Description:
--   SQL initialization script for the 'users' table in MySQL.
--   - Creates the 'users' table to store user information.
--   - Columns: id (auto-increment, primary key), name, email, created_at.
--   - Enforces uniqueness on (id, email) and adds an index on (name, email).
--   - Partitions the table by hash on 'id' into 4 partitions for scalability.
-- Usage:
--   Place this script in the MySQL Docker init directory to auto-run at container startup.
--   Or run manually to initialize the schema before using the application.
-- ============================================================================

-- db/init.sql

CREATE TABLE IF NOT EXISTS users (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_id_email (id, email),
    INDEX idx_name_email (name, email)
)
PARTITION BY HASH(id) PARTITIONS 4;

