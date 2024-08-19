\c indoor_location_estimation;

CREATE TABLE floors (
    id VARCHAR(26) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE pedestrians (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE walking_information (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    pedestrian_id VARCHAR(26) REFERENCES pedestrians(id)
);

CREATE TABLE trajectories (
    id VARCHAR(26) PRIMARY KEY,
    is_walking BOOLEAN NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    floor_id VARCHAR(26) REFERENCES floors(id),
    pedestrian_id VARCHAR(26) REFERENCES pedestrians(id)
);

CREATE TABLE walking_samples (
    id VARCHAR(26) PRIMARY KEY,
    is_converged BOOLEAN NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    trajectory_id VARCHAR(26) REFERENCES trajectories(id),
    walking_information_id VARCHAR(26) UNIQUE REFERENCES walking_information(id)
);

