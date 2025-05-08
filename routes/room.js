const express = require('express');
const router = express.Router();
const Room = require('../models/room');

router.post('/', async (req, res) => {
  const { name, lab, size } = req.body;
  try {
    const room = await Room.create({
      name,
      lab: lab === 'true' || lab === true, // HTML form sends "on"/undefined
      size: parseInt(size),
    });
    res.json(room);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/', async (_req, res) => {
  try {
    const rooms = await Room.findAll();
    res.json(rooms);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
