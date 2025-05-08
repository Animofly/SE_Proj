const express = require('express');
const router = express.Router();
const Course = require('../models/course');

router.post('/', async (req, res) => {
  const { name } = req.body;
  try {
    const course = await Course.create(name);
    res.json(course);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/', async (_req, res) => {
  try {
    const courses = await Course.findAll();
    res.json(courses);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
