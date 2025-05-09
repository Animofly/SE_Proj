const express = require('express');
const path = require('path');
const pool = require('./db');
require('dotenv').config();

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public'))); // Serve HTML forms

// Routes
app.use('/professors', require('./routes/add_professor'));
app.use('/courses', require('./routes/add_course'));
app.use('/rooms', require('./routes/add_room'));
app.use('/groups', require('./routes/add_classgroup'));
app.use('/classes', require('./routes/add_class'));

// Default route
app.get('/', (req, res) => {
  res.send('Welcome to the Timetable Management API');
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
