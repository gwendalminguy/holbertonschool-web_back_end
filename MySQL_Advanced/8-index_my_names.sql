-- Creates an index for table names with first name letter
CREATE INDEX idx_name_first USING BTREE
ON names (name (1))
