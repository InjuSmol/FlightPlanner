import React, { useState, useEffect } from 'react';
import { getAirports } from '../services/airportService';

const AirportList = () => {
    const [airports, setAirports] = useState([]);

    useEffect(() => {
        const fetchAirports = async () => {
            try {
                const data = await getAirports();
                setAirports(data);
            } catch (error) {
                console.error('Error fetching airports:', error);
            }
        };

        fetchAirports();
    }, []);

    return (
        <div>
            <h2>Airports</h2>
            <ul>
                {airports.map((airport) => (
                    <li key={airport.code}>
                        {airport.code} - {airport.latitudeDegrees}°{airport.latitudeMinutes}' / {airport.longitudeDegrees}°{airport.longitudeMinutes}'
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AirportList;
