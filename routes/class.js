const express = require('express');
const router = express.Router();
const Class = require('../models/class');

router.post('/', async (req, res) => {
  const { prof_id, course, duration, group_id } = req.body;
  try {
    const newClass = await Class.create({
      prof_id: parseInt(prof_id),
      course: parseInt(course),
      duration: parseInt(duration),
      group_id: parseInt(group_id),
    });
    res.json(newClass);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/', async (_req, res) => {
  try {
    const classes = await Class.findAll();
    res.json(classes);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
