import React, { useState, useEffect } from 'react';
import axios from 'axios';

function GolfCourseList() {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        axios.get('/api/golfcourses/')
            .then(response => setCourses(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            {courses.map(course => (
                <div key={course.id}>{course.name} - {course.location}</div>
            ))}
        </div>
    );
}

export default GolfCourseList;