const express = require('express');
const userController = require('./controllers/userController');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Routes
app.get('/users', userController.getAllUsers);
app.get('/users/:userId', userController.getUserById);
app.post('/users', userController.createUser);
app.put('/users/:userId', userController.updateUser);
app.delete('/users/:userId', userController.deleteUser);

// Start server
app.listen(PORT, () => {
  console.log(`User service is running on port ${PORT}`);
});
