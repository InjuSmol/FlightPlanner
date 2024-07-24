import axios from 'axios';

const API_URL = '/api/trips';

export const addStop = async (tripId, airportCode) => {
    const response = await axios.post(`${API_URL}/add-stop`, { tripId, airportCode });
    return response.data;
};

export const getTrip = async (tripId) => {
    const response = await axios.get(`${API_URL}/${tripId}`);
    return response.data;
};

export const calculateTripDistance = async (tripId) => {
    const response = await axios.get(`${API_URL}/${tripId}/distance`);
    return response.data;
};
