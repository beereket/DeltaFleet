<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="form.username" placeholder="Username" required />
      <input v-model="form.email" placeholder="Email" type="email" required />
      <input v-model="form.password" placeholder="Password" type="password" required />
      <select v-model="form.role">
        <option value="admin">Admin</option>
        <option value="driver">Driver</option>
        <option value="manager">Manager</option>
      </select>
      <button type="submit">Register</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({ username: '', email: '', password: '', role: 'driver' })
const message = ref('')

async function register() {
  try {
    const res = await axios.post('http://localhost:8000/api/register/', form.value)
    message.value = 'User registered successfully!'
  } catch (err) {
    message.value = err.response?.data?.detail || 'Error registering user'
  }
}
</script>
