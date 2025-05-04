<template>
  <div class="auth-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="form.username" placeholder="Username" required />
      <input v-model="form.password" placeholder="Password" type="password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({ username: '', password: '' })
const message = ref('')

async function login() {
  try {
    const res = await axios.post('http://localhost:8000/api/login/', form.value)
    localStorage.setItem('access_token', res.data.access)
    localStorage.setItem('refresh_token', res.data.refresh)
    message.value = 'Login successful!'
  } catch (err) {
    message.value = err.response?.data?.detail || 'Login failed'
  }
}
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 30px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.auth-container h2 {
  text-align: center;
  margin-bottom: 20px;
}
.auth-container input {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.auth-container button {
  width: 100%;
  padding: 10px;
  background-color: #42b983;
  border: none;
  color: white;
  font-weight: bold;
  cursor: pointer;
  border-radius: 5px;
}
.auth-container button:hover {
  background-color: #369b6b;
}
.auth-container p {
  margin-top: 10px;
  text-align: center;
  color: #555;
}
</style>
