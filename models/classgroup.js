const pool = require('../db');

module.exports = {
  create: async ({ name, size }) => {
    const result = await pool.query(
      'INSERT INTO ClassGroup (name, size) VALUES ($1, $2) RETURNING *',
      [name, size]
    );
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM ClassGroup');
    return result.rows;
  }
};
