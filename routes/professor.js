const express = require('express');
const router = express.Router();
const Professor = require('../models/professor');

router.post('/', async (req, res) => {
  const { name } = req.body;
  try {
    const prof = await Professor.create(name);
    res.json(prof);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/', async (_req, res) => {
  try {
    const data = await Professor.findAll();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
