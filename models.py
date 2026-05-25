from database import cursor, conn

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    check_in DATE,
    check_out DATE,
    room_type VARCHAR(50),
    guests INTEGER,
    requests TEXT
)
""")

conn.commit()