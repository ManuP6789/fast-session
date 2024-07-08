<template>
  <header>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/books">Books</router-link></li>
        <li><router-link to="/ping">Ping</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
header {
  background-color: #333;
  padding: 10px 0;
}
nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
}
nav ul li {
  margin: 0 15px;
}
nav ul li a {
  color: #fff;
  text-decoration: none;
}
nav ul li a.router-link-exact-active {
  font-weight: bold;
}
</style>
