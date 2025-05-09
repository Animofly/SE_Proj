const express = require('express');
const router = express.Router();
const pool = require('../db');

router.post('/', async (req, res) => {
  const { name } = req.body;
  await pool.query('INSERT INTO course (name) VALUES ($1)', [name]);
  res.redirect('/course.html');
});

router.get('/', async (req, res) => {
  const result = await pool.query('SELECT * FROM course');
  res.json(result.rows);
});

router.get('/:id', async (req, res) => {
  const result = await pool.query('SELECT * FROM course WHERE id = $1', [req.params.id]);
  res.json(result.rows[0]);
});

router.put('/:id', async (req, res) => {
  const { name } = req.body;
  await pool.query('UPDATE course SET name = $1 WHERE id = $2', [name, req.params.id]);
  res.send('Course updated');
});

router.delete('/:id', async (req, res) => {
  await pool.query('DELETE FROM course WHERE id = $1', [req.params.id]);
  res.send('Deleted');
});

module.exports = router;
