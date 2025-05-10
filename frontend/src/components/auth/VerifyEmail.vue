<template>
  <div>
    <h2>Email Verification</h2>
    <p v-if="loading">Verifying your email...</p>
    <p v-if="success" style="color: green;">🎉 Email verified successfully! You can now log in.</p>
    <p v-if="error" style="color: red;">❌ Verification failed. The link may be invalid or expired.</p>
    <button v-if="success" @click="$router.push('/login')">Go to Login</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading: true,
      success: false,
      error: false,
    };
  },
  async created() {
    const { uidb64, token } = this.$route.params;
    try {
      await axios.get(`http://127.0.0.1:8000/api/verify-email/${uidb64}/${token}/`);
      this.success = true;
    } catch (err) {
      this.error = true;
    } finally {
      this.loading = false;
    }
  }
};
</script>
