-- Write your PostgreSQL query statement below
WITH PositiveTest AS (
    SELECT patient_id, test_date FROM covid_tests WHERE result = 'Positive'
),
NegativeTest AS (
    SELECT patient_id, test_date FROM covid_tests WHERE result = 'Negative'
),
RecoveredPatients AS(
    SELECT PositiveTest.patient_id, 
        MIN(NegativeTest.test_date) - MIN(PositiveTest.test_date) as recovery_time
    FROM PositiveTest 
    JOIN NegativeTest ON PositiveTest.patient_id = NegativeTest.patient_id
    WHERE PositiveTest.test_date < NegativeTest.test_date
    GROUP BY PositiveTest.patient_id
)
SELECT patients.patient_id, patients.patient_name, patients.age, 
    RecoveredPatients.recovery_time
FROM patients
JOIN RecoveredPatients ON patients.patient_id = RecoveredPatients.patient_id
ORDER BY recovery_time, patients.patient_name ASC