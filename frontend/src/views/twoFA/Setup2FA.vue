<template>
  <div>
    <h2>Setup Two-Factor Authentication</h2>
    <div v-if="qrCode">
      <p><strong>📲 Scan this QR code using Google Authenticator, Authy, or Microsoft Authenticator. Do NOT scan with the iPhone camera app.</strong></p>
      <img :src="qrCode" alt="QR Code" />
      <input v-model="otpCode" placeholder="Enter OTP Code from Authenticator App" />
      <button @click="verify2FA">Verify & Enable 2FA</button>
    </div>
    <button @click="get2FASetup">Generate QR Code</button>
  </div>
</template>

<script>
import authService from "@/services/authService";

export default {
  data() {
    return { qrCode: null, otpCode: '' };
  },
  methods: {
    async get2FASetup() {
      const token = localStorage.getItem('access');
      const response = await authService.get2FASetup(token);
      this.qrCode = `data:image/png;base64,${response.data.qr_code_base64}`;
    },
    async verify2FA() {
      const token = localStorage.getItem('access');
      try {
        await authService.verify2FA(token, this.otpCode);
        alert('2FA Enabled Successfully!');
        this.$router.push('/dashboard');
      } catch (err) {
        alert('Invalid OTP Code. Please try again.');
      }
    }
  }
};
</script>
