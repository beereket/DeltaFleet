<template>
  <div>
    <h2>📧 Please Check Your Email</h2>
    <p>We’ve sent a verification link to your email address.</p>
    <p>Click the link in the email to verify your account before logging in.</p>
    <button @click="$router.push('/login')">Go to Login</button>
  </div>
</template>

<script>
export default {};
</script>
