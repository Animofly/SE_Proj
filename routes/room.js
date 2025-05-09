const express = require('express');
const router = express.Router();
const pool = require('../db');

router.post('/', async (req, res) => {
  const { name, lab, size } = req.body;
  await pool.query('INSERT INTO room (name, lab, size) VALUES ($1, $2, $3)', [name, lab === 'on', size]);
  res.redirect('/room.html');
});

router.get('/', async (req, res) => {
  const result = await pool.query('SELECT * FROM room');
  res.json(result.rows);
});

router.get('/:name', async (req, res) => {
  const result = await pool.query('SELECT * FROM room WHERE name = $1', [req.params.name]);
  res.json(result.rows[0]);
});

router.put('/:name', async (req, res) => {
  const { lab, size } = req.body;
  await pool.query('UPDATE room SET lab = $1, size = $2 WHERE name = $3', [lab === 'on', size, req.params.name]);
  res.send('Room updated');
});

router.delete('/:name', async (req, res) => {
  await pool.query('DELETE FROM room WHERE name = $1', [req.params.name]);
  res.send('Deleted');
});

module.exports = router;
