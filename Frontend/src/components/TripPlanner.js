import React, { useState } from 'react';
import { addStop, calculateTripDistance } from '../services/tripService';

const TripPlanner = () => {
    const [tripId, setTripId] = useState('');
    const [airportCode, setAirportCode] = useState('');
    const [distance, setDistance] = useState(null);

    const handleAddStop = async () => {
        try {
            await addStop(tripId, airportCode);
            // Optionally, fetch updated trip info
        } catch (error) {
            console.error('Error adding stop:', error);
        }
    };

    const handleCalculateDistance = async () => {
        try {
            const { totalDistance } = await calculateTripDistance(tripId);
            setDistance(totalDistance);
        } catch (error) {
            console.error('Error calculating distance:', error);
        }
    };

    return (
        <div>
            <h2>Plan Your Trip</h2>
            <input
                type="text"
                placeholder="Trip ID"
                value={tripId}
                onChange={(e) => setTripId(e.target.value)}
            />
            <input
                type="text"
                placeholder="Airport Code"
                value={airportCode}
                onChange={(e) => setAirportCode(e.target.value)}
            />
            <button onClick={handleAddStop}>Add Stop</button>
            <button onClick={handleCalculateDistance}>Calculate Distance</button>
            {distance !== null && <p>Total Distance: {distance} miles</p>}
        </div>
    );
};

export default TripPlanner;
