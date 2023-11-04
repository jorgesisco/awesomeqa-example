// services/ticketService.js
import axios from 'axios';

export async function fetchTickets(url) {
  try {
    const response = await axios.get(url);
    // Transform the data here if needed
    return response.data.data;
  } catch (error) {
    // Handle or throw the error
    throw error;
  }
}
