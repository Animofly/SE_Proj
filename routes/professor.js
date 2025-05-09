const express = require('express');
const router = express.Router();
const pool = require('../db');

// Create
router.post('/', async (req, res) => {
  const { name } = req.body;
  await pool.query('INSERT INTO professor (name) VALUES ($1)', [name]);
  res.redirect('/professor.html');
});

// Read all
router.get('/', async (req, res) => {
  const result = await pool.query('SELECT * FROM professor');
  res.json(result.rows);
});

// Read one
router.get('/:id', async (req, res) => {
  const result = await pool.query('SELECT * FROM professor WHERE id = $1', [req.params.id]);
  res.json(result.rows[0]);
});

// Update
router.put('/:id', async (req, res) => {
  const { name } = req.body;
  await pool.query('UPDATE professor SET name = $1 WHERE id = $2', [name, req.params.id]);
  res.send('Professor updated');
});

// Delete
router.delete('/:id', async (req, res) => {
  await pool.query('DELETE FROM professor WHERE id = $1', [req.params.id]);
  res.send('Deleted');
});

module.exports = router;
