<template>
  <div>
    <h2>Register</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="email" type="email" placeholder="Email" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="register">Register</button>
  </div>
</template>

<script>
import authService from "@/services/authService";

export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async register() {
      try {
        await authService.register({
          username: this.username,
          email: this.email,
          password: this.password
        });
        alert('Registration successful! Please check your email for verification.');
        this.$router.push('/login');
      } catch (err) {
        alert('Registration failed: ' + (err.response?.data?.detail || 'Unknown error'));
      }
    }
  }
};
</script>
