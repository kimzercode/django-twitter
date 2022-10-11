<template>
    <form @submit.prevent="handleSubmit">
        <label for="name">Name</label>
        <input v-model.trim.lazy="name" type="text">
        <label for="message">Message</label>
        <input v-model.trim.lazy="message" type="text"> <br>
        <button type="submit">Tweet</button>
    <p v-show="error" class="error">{{error}}</p>
    </form>
</template>

<script>
    export default {
        data() {
            return {
                name: '',
                message: '',
                error: ''
            }
        },
        methods: {
            async handleSubmit() {
                if(this.name.length<1 || this.message.length<1) return this.error = 'Enter a message and a name!!!'
                if(this.message.length>50) return this.error = "Message can't exceed 50 characters!!!"
                const url = " http://127.0.0.1:8000/api/tweets/"
                try {
                    const response = await fetch(url, {
                        method: 'POST',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({"name": this.name, "message": this.message,})
                    })
                    if (response.status !== 201 ) throw 'An error occured on the server'
                    const data = await response.json()
                    data.created_at = new Date(data.created_at).toLocaleString()
                    this.$emit('newTweet', data)
                } catch (error) {
                    return this.error = error
                }
                document.activeElement.blur()
                this.error = ''
                this.name = ''
                this.message = ''
            
            }
        }
}
</script>

<style>
input{
    margin: 0 16px 0 8px;
}
button {
    display: block;
    width: 100%;
    margin: 16px 0;
    padding: 8px;
    background-color: #f0f0f0;
    border: none;
    color: black;
    font-size: 16px;
    text-transform: uppercase;
    font-weight: bolder;
}

.error {
    color: rgb(189, 0, 0);
    border: 2px solid rgb(188, 0, 0);
    padding: 8px;
}
</style>