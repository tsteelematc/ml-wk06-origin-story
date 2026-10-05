CREATE TABLE inventory AS
SELECT *
FROM read_csv_auto('inventory.csv');

SELECT
    buyer,

    -- health food category
    protein_shake +
    powerade +
    protein_bar +
    vitamins AS health_food,

    -- apparel category
    nike_sneakers +
    adidas_boots AS apparel,

    -- digital category
    fitbit +
    fitness_watch AS digital

FROM inventory;
