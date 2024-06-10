select
    patient_id,
    patient_name,
    conditions
from patients
where conditions ~ '\mDIAB1';
