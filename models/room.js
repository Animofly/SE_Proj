const pool = require('../db');

module.exports = {
  create: async ({ name, lab, size }) => {
    const result = await pool.query(
      'INSERT INTO Room (name, lab, size) VALUES ($1, $2, $3) RETURNING *',
      [name, lab, size]
    );
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM Room');
    return result.rows;
  }
};
