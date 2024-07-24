import React from 'react';
import AirportList from '../components/AirportList';
import TripPlanner from '../components/TripPlanner';

const HomePage = () => {
    return (
        <div>
            <h1>Trip Planner</h1>
            <AirportList />
            <TripPlanner />
        </div>
    );
};

export default HomePage;
