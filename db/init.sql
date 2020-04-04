CREATE TABLE transactions (
    time TIMESTAMP WITH TIME ZONE,
    bsb_acc_num TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    payee TEXT NOT NULL,
    description TEXT,
    category TEXT,
    tags TEXT,
    subtotal MONEY,
    currency TEXT,
    subtotal_transaction_currency MONEY,
    fee MONEY,
    round_up MONEY,
    total MONEY,
    payment_method TEXT,
    settled_date DATE NOT NULL
);
