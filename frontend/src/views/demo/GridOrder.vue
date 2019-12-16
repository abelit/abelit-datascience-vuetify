<template>
    <v-container class="d-flex">
      <v-card width="100" height="100" align="center" class="order-1 mx-2">1</v-card>
      <v-card width="100" height="200" align="center" class="order-1 mx-2">3</v-card>
      <v-card width="100" height="150" align="center" class="order-1 mx-2">2</v-card>
      <v-card width="100" height="100" align="center" class="order-1 mx-2">4</v-card>
    </v-container>
</template>

<script>
export default {
    methods: {
        isInteger(num) {
            if (num % 1 === 0) {
                return true
            }
            return false
        }
    },
    mounted() {
        console.log("hi")
        console.log(this.isInteger(3.0))
        console.log(3.5%1)
    }
}
</script>