import React, { useState } from 'react';
import TripStops from '../components/TripStops';

const TripPage = () => {
    const [tripId, setTripId] = useState('');

    return (
        <div>
            <h1>Trip Details</h1>
            <input
                type="text"
                placeholder="Trip ID"
                value={tripId}
                onChange={(e) => setTripId(e.target.value)}
            />
            {tripId && <TripStops tripId={tripId} />}
        </div>
    );
};

export default TripPage;
