-- Write your PostgreSQL query statement below
SELECT sample_id, dna_sequence, species, 
    CASE WHEN dna_sequence like 'ATG%' THEN 1 ELSE 0 END as has_start,
    CASE WHEN (dna_sequence like '%TAA' OR dna_sequence like '%TAG' OR dna_sequence like '%TGA') THEN 1 ELSE 0 END as has_stop,
    CASE WHEN dna_sequence like '%ATAT%' THEN 1 ELSE 0 END as has_atat,
    CASE WHEN dna_sequence like '%GGG%' THEN 1 ELSE 0 END as has_ggg
FROM Samples
ORDER BY sample_id ASC