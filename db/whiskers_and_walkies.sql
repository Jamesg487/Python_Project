DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    species_specialism VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255),
    telephone VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    date_of_birth DATE,
    species VARCHAR(255),
    treatment_notes TEXT,
    nervous BOOLEAN
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    pet_id INT REFERENCES pets(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    date DATE,
    start_time TIME,
    duration INT,
    appointment_notes TEXT
);