const pool = require('../db');

module.exports = {
  create: async ({ prof_id, course, duration, group_id }) => {
    const result = await pool.query(
      'INSERT INTO Class (prof_id, course, duration, group_id) VALUES ($1, $2, $3, $4) RETURNING *',
      [prof_id, course, duration, group_id]
    );
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM Class');
    return result.rows;
  }
};
