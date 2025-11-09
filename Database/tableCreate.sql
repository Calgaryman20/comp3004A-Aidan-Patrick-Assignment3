CREATE TABLE IF NOT EXISTS students (
	student_id SERIAL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	enrollment_date DATE
);
