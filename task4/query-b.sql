-- Return the mean values of PM2.5 (particulate matter <2.5 micron diameter) & 
-- VPM2.5 (volatile particulate matter <2.5 micron diameter) by each station
-- for the year 2019 for readings taken on or near 08:00 hours (peak traffic intensity).

SELECT 
    `Location`,
    AVG(`PM2.5`) AS average_particulate_matter,
    AVG(`VPM2.5`) AS average_volatile_matter
FROM
    AirQualityMeasures
WHERE
    YEAR(`Date Time`) = 2019
        AND EXTRACT(HOUR FROM `Date Time`) BETWEEN '07: 00' AND '08: 00'
GROUP BY `Location`