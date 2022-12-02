-- Displays the average temperature (in Farenheit)
-- by city ordered by descending temperature.
SELECT `city`, AVG(`value`) as `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
