const pool = require('../db');

module.exports = {
  create: async (name) => {
    const result = await pool.query('INSERT INTO Course (name) VALUES ($1) RETURNING *', [name]);
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM Course');
    return result.rows;
  }
};
