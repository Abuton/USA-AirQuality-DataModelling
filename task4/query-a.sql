-- Return the date/time, station name and the highest recorded value of nitrogen oxide (NOx) found in the dataset for the year 2019.
SELECT 
    `Date Time`, `Location`, MAX(`NOx`) AS MaxNOx
FROM
    AirQualityMeasures
WHERE
    YEAR(`Date Time`) = 2019
GROUP BY `Date Time` , `Location`