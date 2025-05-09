const express = require('express');
const path = require('path');
const pool = require('./db');
require('dotenv').config();

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Routers
app.use('/professors', require('./routes/professor'));
app.use('/courses', require('./routes/course'));
app.use('/rooms', require('./routes/room'));
app.use('/groups', require('./routes/group'));
app.use('/classes', require('./routes/class'));

// Home route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add_professor.html')); // default landing
});

// Form pages
app.get('/professor_form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add_professor.html'));
});
app.get('/course_form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add_course.html'));
});
app.get('/room_form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add_room.html'));
});
app.get('/group_form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add_group.html'));
});
app.get('/class_form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'add_class.html'));
});

// View/Edit pages
app.get('/view_and_edit_professor', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'view_and_edit_professor.html'));
});
app.get('/view_and_edit_course', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'view_and_edit_course.html'));
});
app.get('/view_and_edit_room', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'view_and_edit_room.html'));
});
app.get('/view_and_edit_group', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'view_and_edit_group.html'));
});
app.get('/view_and_edit_class', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'view_and_edit_class.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
