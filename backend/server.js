const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const jwt = require('jsonwebtoken');
const pool = require('./db');

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const JWT_SECRET = process.env.JWT_SECRET || 'supersecretjwtkey';

// Mock OTP verification (in a real app, integrate with Twilio/AWS SNS)
app.post('/api/auth/send-otp', (req, res) => {
  const { phone } = req.body;
  if (!phone) {
    return res.status(400).json({ error: 'Phone number required' });
  }
  // Mocking OTP send
  res.json({ success: true, message: 'OTP sent successfully' });
});

app.post('/api/auth/verify-otp', async (req, res) => {
  const { phone, otp } = req.body;
  if (otp !== '1234') {
    return res.status(400).json({ error: 'Invalid OTP. Use 1234.' });
  }

  try {
    const [rows] = await pool.query('SELECT * FROM users WHERE phone_number = ?', [phone]);
    
    if (rows.length === 0) {
      // User not found, flag for signup flow
      return res.json({ isNewUser: true, message: 'User not found. Please sign up.' });
    }

    const user = rows[0];
    const token = jwt.sign({ id: user.id, phone: user.phone_number }, JWT_SECRET, { expiresIn: '7d' });

    res.json({ token, isNewUser: false, user: { name: user.name, phone: user.phone_number, id: user.id, createdAt: user.created_at } });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error during OTP verification' });
  }
});

app.post('/api/auth/signup', async (req, res) => {
  const { name, phone, otp } = req.body;
  if (otp !== '1234') {
    return res.status(400).json({ error: 'Invalid OTP. Use 1234.' });
  }
  if (!name || !phone) {
    return res.status(400).json({ error: 'Name and phone are required.' });
  }

  try {
    const [existing] = await pool.query('SELECT * FROM users WHERE phone_number = ?', [phone]);
    if (existing.length > 0) {
      return res.status(400).json({ error: 'User already exists. Please log in.' });
    }

    const [result] = await pool.query('INSERT INTO users (name, phone_number) VALUES (?, ?)', [name, phone]);
    const userId = result.insertId;

    const token = jwt.sign({ id: userId, phone }, JWT_SECRET, { expiresIn: '7d' });

    res.json({ token, user: { id: userId, name, phone }, message: 'Signup successful' });
  } catch (err) {
    console.error('Signup error:', err);
    res.status(500).json({ error: 'Failed to create user' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
