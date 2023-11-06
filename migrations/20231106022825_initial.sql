-- migrate:up
create table credit_card(
   id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
   exp_date DATE NOT NULL,
   holder VARCHAR (355) NOT NULL,
   number VARCHAR (20) NOT NULL,
   cvv VARCHAR (4)
);

-- migrate:down
drop table credit_card;
