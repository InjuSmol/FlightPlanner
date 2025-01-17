import axios from 'axios';

const API_URL = '/api/airports';

export const getAirports = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};
