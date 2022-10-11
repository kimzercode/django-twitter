<script setup>
import { ref } from 'vue'
import NewTweet from './components/NewTweet.vue'
import TweetsTable from './components/TweetsTable.vue'
let tweets = ref([])
let sorted = ref([0])
 const getTweets = async () => {
            const url = " http://127.0.0.1:8000/api/tweets/"
            const response = await fetch(url)
            const data = await response.json()
            data.forEach(tweet=>{
              tweet.created_at = new Date(tweet.created_at).toLocaleString()
            })
            tweets.value = data
        }
getTweets()
function addTweet(tweet) {
  tweets.value.unshift(tweet)
}

function sortByTime() {
  if(sorted.value == 0) {
    tweets.value.sort((b,a)=>b.created_at.localeCompare(a.created_at));
    sorted.value++
  } else {
    tweets.value.sort((b,a)=>a.created_at.localeCompare(b.created_at));
    sorted.value--
  }
}

function sortByName() {
  if(sorted.value == 0) {
    tweets.value.sort((a,b)=>b.name.localeCompare(a.name));
    sorted.value++
  } else {
    tweets.value.sort((a,b)=>a.name.localeCompare(b.name));
    sorted.value--
  }
}
</script>

<template>
  <div class="container">
    <h1>Poor Man's Twitter</h1>
    <NewTweet @newTweet="addTweet"/>
    <TweetsTable :tweets="tweets" @sortByTime="sortByTime" @sortByName="sortByName"/>
  </div>
</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
}
</style>
