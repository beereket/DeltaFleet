import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export default {
    register(user) {
        return axios.post(`${API_URL}register/`, user);
    },
    login(user) {
        return axios.post(`${API_URL}login/`, user);
    },
    get2FASetup(token) {
        return axios.get(`${API_URL}2fa/setup/`, { headers: { Authorization: `Bearer ${token}` } });
    },
    verify2FA(token, otpCode) {
        return axios.post(`${API_URL}2fa/verify/`, { otp_code: otpCode }, { headers: { Authorization: `Bearer ${token}` } });
    },
    disable2FA(token, otpCode) {
        return axios.post(`${API_URL}2fa/disable/`, { otp_code: otpCode }, { headers: { Authorization: `Bearer ${token}` } });
    }
};
