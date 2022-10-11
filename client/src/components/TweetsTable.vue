<template>
    <table>
  <tr>
      <th @click="$emit('sortByTime')">Time</th>
    <th @click="$emit('sortByName')">Name</th>
    <th>Message</th>
  </tr>
  <tr v-for="tweet in tweets" :key="tweet.created_at">
    <td>{{tweet.created_at}}</td>
    <td>{{tweet.name}}</td>
    <td>{{tweet.message}}</td>
  </tr>
</table>
</template>

<script>

    export default {
        props: ['tweets']
    }
</script>

<style>
    table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  margin-top: 16px;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
th:hover {
    cursor: pointer;
    background-color: black;
    color: white;
    transition: all ease .3s;
}
tr:nth-child(even) {
  background-color: #f0f0f0;
}
</style>