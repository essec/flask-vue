<template>
    <div>
        <p>Home page</p>
        <a href="about" class="ui button">about</a>
        <br>
        <br>
        <button @click="getRandom" class="ui button">New random Number</button>
        <br>
        <br>
        <p>Random number from backend: {{ randomNumber }}</p>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    data() {
        return{
            randomNumber : 0
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
        }
    },
    create(){
        this.getRandom()
    }
}
</script>
