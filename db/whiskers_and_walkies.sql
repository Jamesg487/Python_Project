DROP TABLE pets;
DROP TABLE vets;
DROP TABLE owners;

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
    date_of_birth VARCHAR(255),
    type_of_animal VARCHAR(255),
    treatment_note TEXT,
    nervous BOOLEAN
);