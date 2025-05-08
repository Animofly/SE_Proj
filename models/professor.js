const pool = require('../db');

module.exports = {
  create: async (name) => {
    const result = await pool.query('INSERT INTO Professor (name) VALUES ($1) RETURNING *', [name]);
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM Professor');
    return result.rows;
  }
};
