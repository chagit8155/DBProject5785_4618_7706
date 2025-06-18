--======================================================================================
--VIEWS:
-- View #1: Single gym perspective - Individual gym management (Studio ID = 130)
CREATE OR REPLACE VIEW single_gym_management_view AS
SELECT 
    c.course_id,
    co.course_name,
    co.required_experience,
    co.min_age,
    co.price,
    t.day AS class_day,
    t.start_time,
    t.end_time,
    p.person_name AS trainer_name,
    p.gender AS trainer_gender,
    tr.experiencelevel AS trainer_experience,
    c.registrants AS enrollment,
    r.room_name,
    r.room_id,
    r.capacity AS room_capacity
FROM 
    Class c
JOIN Course co ON c.course_id = co.course_id
JOIN TimeSlot t ON c.timeslot_id = t.timeslot_id
JOIN Person p ON c.Id = p.person_id
JOIN Trainer tr ON p.person_id = tr.person_id
JOIN Room r ON c.IdR = r.room_id
JOIN Studio s ON r.studio_id = s.studio_id
WHERE 
    s.studio_id = 130  -- Studio filtering is now correctly applied
ORDER BY 
    t.day, t.start_time;

-- Display data from the first view
SELECT * FROM single_gym_management_view LIMIT 10;

-- Query #1 for the first view: Room capacity report for the single gym
SELECT 
    room_name,
    room_capacity,
    COUNT(course_id) AS total_classes,
    MAX(enrollment) AS max_enrollment,
    ROUND(AVG(enrollment)::numeric, 2) AS avg_enrollment,
    ROUND((MAX(enrollment) * 100.0 / room_capacity)::numeric, 2) AS max_capacity_percent
FROM 
    single_gym_management_view
GROUP BY 
    room_name, room_capacity
ORDER BY 
    max_capacity_percent DESC;


-- Query #2 for the first view: Report on trainers and their experience level in the single gym
SELECT 
    trainer_name,
    trainer_gender,
    trainer_experience,
    COUNT(course_id) AS classes_taught,
    STRING_AGG(DISTINCT course_name, ', ') AS taught_courses,
    SUM(enrollment) AS total_students
FROM 
    single_gym_management_view
GROUP BY 
    trainer_name, trainer_gender, trainer_experience
ORDER BY 
    classes_taught DESC, total_students DESC;


-- View #2: Network perspective - Management of multiple studios across the country
CREATE OR REPLACE VIEW multi_studio_network_view AS
SELECT 
    s.studio_id,
    s.location AS studio_location,
    s.capacity AS studio_capacity,
    c.course_id,
    co.course_name,
    co.price AS course_price,
    ts.day,
    ts.start_time,
    ts.end_time,
    p.person_id AS trainer_id,
    p.person_name AS trainer_name,
    p.gender,
    c.registrants AS enrollment
FROM 
    Room r
JOIN Studio s ON r.studio_id = s.studio_id
JOIN Class c ON c.idr = r.room_id
LEFT JOIN Course co ON c.course_id = co.course_id
LEFT JOIN TimeSlot ts ON c.timeslot_id = ts.timeslot_id
LEFT JOIN Person p ON c.id = p.person_id
LEFT JOIN registers_for rf ON c.timeslot_id = rf.timeslot_id AND c.idr = rf.room_id

ORDER BY 
    s.studio_id, ts.day, ts.start_time;

-- Display data from the second view
SELECT * FROM multi_studio_network_view LIMIT 10;


-- Query #1 for the second view: Performance comparison between different studios
SELECT 
    studio_id,
    studio_location,
    studio_capacity,
    COUNT(DISTINCT course_id) AS total_courses_offered,
    COUNT(DISTINCT CONCAT(day, start_time)) AS total_timeslots,
    COUNT(DISTINCT trainer_id) AS total_trainers,
    SUM(enrollment) AS total_enrollment,
    ROUND(AVG(enrollment)::numeric, 2) AS avg_class_size,
    ROUND(AVG(course_price)::numeric, 2) AS avg_course_price
FROM 
    multi_studio_network_view
WHERE 
    course_id IS NOT NULL
GROUP BY 
    studio_id, studio_location, studio_capacity
ORDER BY 
    total_enrollment DESC;

-- Query #2 for the second view: Analysis of popular activity times across all studios
SELECT 
    day,
    start_time,
    COUNT(DISTINCT studio_id) AS studios_with_classes,
    COUNT(DISTINCT course_id) AS unique_courses,
    SUM(enrollment) AS total_enrollment,
    ROUND(AVG(enrollment)::numeric, 2) AS avg_enrollment
FROM 
    multi_studio_network_view
WHERE 
    course_id IS NOT NULL
GROUP BY 
    day, start_time
ORDER BY 
    total_enrollment DESC, day, start_time;