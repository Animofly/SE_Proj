const express = require('express');
const router = express.Router();
const pool = require('../db');

router.post('/', async (req, res) => {
  const { prof_id, course, duration, group_id } = req.body;
  await pool.query(
    'INSERT INTO class (prof_id, course, duration, "group") VALUES ($1, $2, $3, $4)',
    [prof_id, course, duration, group_id]
  );
  res.redirect('/class.html');
});

router.get('/', async (req, res) => {
  const result = await pool.query('SELECT * FROM class');
  res.json(result.rows);
});

router.get('/:id', async (req, res) => {
  const result = await pool.query('SELECT * FROM class WHERE id = $1', [req.params.id]);
  res.json(result.rows[0]);
});

router.put('/:id', async (req, res) => {
  const { prof_id, course, duration, group_id } = req.body;
  await pool.query(
    'UPDATE class SET prof_id = $1, course = $2, duration = $3, "group" = $4 WHERE id = $5',
    [prof_id, course, duration, group_id, req.params.id]
  );
  res.send('Class updated');
});

router.delete('/:id', async (req, res) => {
  await pool.query('DELETE FROM class WHERE id = $1', [req.params.id]);
  res.send('Deleted');
});

module.exports = router;
