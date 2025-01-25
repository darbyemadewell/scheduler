"use client";

import { useState, useEffect } from "react";

export default function DailySchedule() {
    const [events, setEvents] = useState([])
    const [currentDate, setCurrentDate] = useState("");

    useEffect(() => {
        const date = new Date();
        setCurrentDate(date.toDateString());
    }, []);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/events/')
            .then(response => response.json())
            .then(json => setEvents(json))
            .catch(error => console.error(error))
    }, []);

    return (
        <div>
            <h2 className="text-2xl mb-2">{currentDate}</h2>
            <div>
                {events.map((event) => {
                    const startDate = new Date(event.start_time);
                    const startDateMS = startDate.getTime();
                    const duration = event.duration.split(":");
                    const durationMS =  (parseInt(duration[0], 10) * 60 * 60 * 1000) +
                                            (parseInt(duration[1], 10) * 60 * 1000) + 
                                            (parseInt(duration[2], 10) * 1000);
                    const endDate = new Date();
                    endDate.setTime(startDateMS + durationMS);

                    return (
                        <div key={event.start_time}>
                            <p className="text-sm text-slate-400">{startDate.toLocaleTimeString()} - {endDate.toLocaleTimeString()}</p>
                            <p className="text-lg">{event.name}</p>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}