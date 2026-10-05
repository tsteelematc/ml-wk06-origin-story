CREATE TABLE animals AS
SELECT *
FROM read_csv_auto('animals.csv');

-- animals sqlite sql
SELECT
    meat_eater,
    legs,
    tail,
    COUNT(*) AS animal_count,

    printf(
        '%02d:%02d',
        AVG(
            CAST(substr(race_time, 1, instr(race_time, ':') - 1) AS INT) * 60 +
            CAST(substr(race_time, instr(race_time, ':') + 1) AS INT)
        ) / 60,
        AVG(
            CAST(substr(race_time, 1, instr(race_time, ':') - 1) AS INT) * 60 +
            CAST(substr(race_time, instr(race_time, ':') + 1) AS INT)
        ) % 60
    ) AS avg_race_time_mmss

FROM animals
GROUP BY meat_eater, legs, tail
ORDER BY meat_eater;
