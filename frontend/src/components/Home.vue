<template>
    <div>
        <p>Home page</p>
        <a href="about" class="ui button">about</a> <a href="books" class="ui button">Book</a>
        <br>
        <br>
        <button @click="getRandom" class="ui button">New random Number</button>
        <br>
        <br>
        <p>Random number from backend: {{ randomNumber }}</p>
        <h1>Input your Book</h1>
        <form class="ui form" method="POST">
            <input type="text" v-model="book">
        </form>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    name : 'Home',
    data() {
        return{
            randomNumber : 0,
            title,
            author
        }
    },
    methods: {
        // getRandomInt (min, max){
        //     min = Math.ceil(min)
        //     max = Math.floor(max)
        //     return Math.floor(Math.random() * (max - min + 1)) + min
        // },
        getRandom(){
            // this.randomNumber = this.getRandomInt(1, 100)
            this.randomNumber = this.getRandomFromBackend()
        },
        getRandomFromBackend(){
            const path = `http://localhost:5000/api/random`
            axios.get(path)
            .then(response => {
                this.randomNumber = response.data.randomNumber
            })
            .catch(error => {
                console.log(error)
            })
        },
        setBook(){
            const path = `http://localhost:5000/api/book`
            axios.post(path)
            .then()
        }
    },
    create(){
        this.getRandom()
    }
}
</script>
