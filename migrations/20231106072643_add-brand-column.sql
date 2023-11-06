-- migrate:up
ALTER TABLE credit_card ADD column brand VARCHAR(20) NOT NULL;

-- migrate:down
ALTER TABLE credit_card DROP column brand;
