const express = require('express');
const router = express.Router();
const Group = require('../models/classgroup');

router.post('/', async (req, res) => {
  const { name, size } = req.body;
  try {
    const group = await Group.create({ name, size: parseInt(size) });
    res.json(group);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/', async (_req, res) => {
  try {
    const groups = await Group.findAll();
    res.json(groups);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
