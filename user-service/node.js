const axios = require('axios');

// Example: Making a GET request to retrieve user details by ID
async function getUserById(userId) {
  try {
    const response = await axios.get(`http://user-service:3000/users/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user:', error.response.data);
    throw error;
  }
}
