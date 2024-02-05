
    CREATE TABLE IF NOT EXISTS authors (
        author_id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_born INTEGER
    );

    CREATE TABLE IF NOT EXISTS books (
        book_id TEXT PRIMARY KEY,
        title TEXT,
        year_published INTEGER,
        author_id TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
