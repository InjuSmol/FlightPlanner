import React, { useState, useEffect } from 'react';
import { getTrip } from '../services/tripService';

const TripStops = ({ tripId }) => {
    const [trip, setTrip] = useState(null);

    useEffect(() => {
        const fetchTrip = async () => {
            try {
                const data = await getTrip(tripId);
                setTrip(data);
            } catch (error) {
                console.error('Error fetching trip:', error);
            }
        };

        fetchTrip();
    }, [tripId]);

    if (!trip) return <p>Loading...</p>;

    return (
        <div>
            <h2>Trip Stops</h2>
            <ul>
                {trip.stops.map((stop) => (
                    <li key={stop.code}>
                        {stop.code} - {stop.latitudeDegrees}°{stop.latitudeMinutes}' / {stop.longitudeDegrees}°{stop.longitudeMinutes}'
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TripStops;
