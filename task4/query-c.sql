-- Extend the previous query to show these values for all stations in the years 2010 to 2019.

SELECT 
    `Location`,
    AVG(`PM2.5`) AS average_particulate_matter,
    AVG(`VPM2.5`) AS average_volatile_matter
FROM
    AirQualityMeasures
WHERE
    YEAR(`Date Time`) BETWEEN 2010 AND 2019
        AND EXTRACT(HOUR FROM `Date Time`) BETWEEN '07: 00' AND '08: 00'
GROUP BY `Location`