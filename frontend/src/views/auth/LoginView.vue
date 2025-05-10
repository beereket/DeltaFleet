<template>
  <div>
    <h2>Login</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <div v-if="requires2FA">
      <input v-model="otpCode" placeholder="Enter OTP Code" />
    </div>
    <button @click="login">{{ requires2FA ? 'Verify OTP' : 'Login' }}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      otpCode: '',
      requires2FA: false,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/two-step-login/', {
          username: this.username,
          password: this.password,
          otp_code: this.requires2FA ? this.otpCode : null,
        });

        if (response.data.requires_2fa) {
          this.requires2FA = true;
        } else if (response.data.access) {
          localStorage.setItem('access', response.data.access);
          localStorage.setItem('refresh', response.data.refresh);
          this.$router.push('/dashboard');
        }
      } catch (err) {
        alert('Login failed: ' + (err.response?.data?.detail || 'Unknown error'));
      }
    }
  }
};
</script>
