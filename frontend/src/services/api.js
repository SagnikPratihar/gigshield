import axios from 'axios';

// Mock responses since backend is not fully integrated for some features
const MOCK_DELAY = 800;
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const API_URL = 'http://localhost:5000/api';

export const authApi = {
  sendOtp: async (phone) => {
    const response = await axios.post(`${API_URL}/auth/send-otp`, { phone });
    return response.data;
  },
  verifyOtp: async (phone, otp) => {
    const response = await axios.post(`${API_URL}/auth/verify-otp`, { phone, otp });
    return response.data;
  },
  signup: async (name, phone, otp) => {
    const response = await axios.post(`${API_URL}/auth/signup`, { name, phone, otp });
    return response.data;
  }
};

export const workerApi = {
  register: async (workerData) => {
    await delay(MOCK_DELAY);
    return { success: true, worker: workerData };
  },
  getDashboard: async () => {
    await delay(MOCK_DELAY);
    return {
      status: "ACTIVE",
      coveredDisruptions: 0,
      activeEvents: [
        { type: "HEAVY_RAIN", zone: "Koramangala", severity: "42mm/hr" }
      ]
    };
  }
};

export const policyApi = {
  getPlans: async () => {
    await delay(MOCK_DELAY);
    return [
      { id: "basic", name: "Basic", basePrice: 29, aiPrice: 29, maxDaily: 500, badge: "", label: "Up to 20 hrs/week" },
      { id: "standard", name: "Standard", basePrice: 49, aiPrice: 49, maxDaily: 900, badge: "HIGH RISK WEEK", label: "Up to 40 hrs/week" },
      { id: "pro", name: "Pro", basePrice: 99, aiPrice: 110, maxDaily: 1500, badge: "", label: "60+ hrs/week" }
    ];
  },
  purchasePlan: async (planId) => {
    await delay(MOCK_DELAY);
    return { success: true, policyId: "POL-999-1" };
  }
};

export const claimsApi = {
  getClaims: async () => {
    await delay(MOCK_DELAY);
    return [
      { id: "CLM-001", date: "2026-03-25", amount: 280, reason: "Heavy Rain > 35mm/hr", status: "SUCCESS" },
      { id: "CLM-002", date: "2026-03-10", amount: 420, reason: "Sudden Bandh", status: "SUCCESS" }
    ];
  }
};
