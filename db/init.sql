CREATE TABLE category_types (
    name TEXT NOT NULL,
    PRIMARY KEY (name)
);

INSERT INTO category_types
    (name)
VALUES
    ('Uncategorised'),
    ('Personal'),
    ('Transport'),
    ('Good Life'),
    ('Home');

CREATE TABLE categories (
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    PRIMARY KEY (name),
    FOREIGN KEY (type) REFERENCES category_types(name)
);

INSERT INTO categories
    (name, type)
VALUES
    ('', 'Uncategorised'),
    ('Clothing & Accessories', 'Personal'),
    ('Education & Student Loans', 'Personal'),
    ('Repayments', 'Transport'),
    ('Public Transport', 'Home'),
    ('Mobile Phone', 'Personal'),
    ('Gifts & Charity', 'Personal'),
    ('Hair & Beauty', 'Personal'),
    ('News, Magazines & Books', 'Personal'),
    ('Hobbies', 'Good Life'),
    ('Maintenance & Improvements', 'Home'),
    ('Health & Medical', 'Personal'),
    ('Homeware & Appliances', 'Home'),
    ('Booze', 'Good Life'),
    ('Groceries', 'Home'),
    ('Internet', 'Home'),
    ('Takeaway', 'Good Life'),
    ('Events & Gigs', 'Good Life'),
    ('Investments', 'Personal'),
    ('Life Admin', 'Personal'),
    ('Taxis & Share Cars', 'Transport'),
    ('Technology', 'Personal'),
    ('Fuel', 'Transport'),
    ('TV, Music & Streaming', 'Good Life'),
    ('Holidays & Travel', 'Good Life'),
    ('Car Insurance, Rego & Maintenance', 'Transport'),
    ('Tolls', 'Transport'),
    ('Pubs & Bars', 'Good Life'),
    ('Parking', 'Transport'),
    ('Fitness & Wellbeing', 'Personal'),
    ('Restaurants & Cafes', 'Good Life'),
    ('Apps, Games & Software', 'Good Life'),
    ('Lottery & Gambling', 'Good Life'),
    ('Tobacco & Vaping', 'Good Life'),
    ('Adult', 'Good Life'),
    ('Children & Family', 'Personal'),
    ('Pets', 'Home'),
    ('Rates & Insurace', 'Home'),
    ('Rent & Mortgage', 'Home'),
    ('Utilities', 'Home'),
    ('Cycling', 'Transport');

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
    settled_date DATE NOT NULL,
    FOREIGN KEY (category) REFERENCES categories(name)
);
