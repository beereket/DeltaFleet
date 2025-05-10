<template>
  <div>
    <h2>Disable Two-Factor Authentication</h2>
    <input v-model="otpCode" placeholder="Enter OTP Code" />
    <button @click="disable2FA">Disable 2FA</button>
  </div>
</template>

<script>
import authService from "@/services/authService";

export default {
  data() {
    return { otpCode: '' };
  },
  methods: {
    async disable2FA() {
      const token = localStorage.getItem('access');
      await authService.disable2FA(token, this.otpCode);
      alert('2FA Disabled.');
      this.$router.push('/dashboard');
    }
  }
};
</script>
