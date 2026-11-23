-- Creates an index for table names with first name letter and score
CREATE INDEX idx_name_first_score USING BTREE
ON names (name (1), score)
