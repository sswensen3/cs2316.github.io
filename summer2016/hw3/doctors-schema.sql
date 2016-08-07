create table if not exists doctor (
  doctor_id integer primary key autoincrement,
  first_name text,
  last_name text,
  specialty text
);

create table if not exists patient (
  patient_id integer primary key,
  first_name text,
  last_name text,
  doctor_id integer references doctor(doctor_id)
);

create table if not exists visit (
  doctor_id integer references doctor(doctor_id),
  patient_id integer references patient(patient_id),
  date text
);
