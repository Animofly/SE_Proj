const express = require('express');
const router = express.Router();
const pool = require('../db');

router.post('/', async (req, res) => {
  const { name, size } = req.body;
  await pool.query('INSERT INTO classgroup (name, size) VALUES ($1, $2)', [name, size]);
  res.redirect('/group.html');
});

router.get('/', async (req, res) => {
  const result = await pool.query('SELECT * FROM classgroup');
  res.json(result.rows);
});

router.get('/:id', async (req, res) => {
  const result = await pool.query('SELECT * FROM classgroup WHERE id = $1', [req.params.id]);
  res.json(result.rows[0]);
});

router.put('/:id', async (req, res) => {
  const { name, size } = req.body;
  await pool.query('UPDATE classgroup SET name = $1, size = $2 WHERE id = $3', [name, size, req.params.id]);
  res.send('Group updated');
});

router.delete('/:id', async (req, res) => {
  await pool.query('DELETE FROM classgroup WHERE id = $1', [req.params.id]);
  res.send('Deleted');
});

module.exports = router;
