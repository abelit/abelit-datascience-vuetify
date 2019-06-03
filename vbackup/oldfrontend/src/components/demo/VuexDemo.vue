<template>
    <div>
        <h1>{{count}}</h1>
        <div><button class="btn-primary" @click="mincrement">...mapMututions+</button></div>
        <div><button class="btn-primary" @click="adecrement">...mapActions-</button></div>
        <div><button class="btn-primary" @click="tincrement">method&...mapAction+</button></div>
        <div><button class="btn-primary" @click="tdecrement">this.$store.commit-</button></div>
        <div><button class="btn-primary" @click="nincrement">method&...mapMututions+</button></div>
    </div>
</template>


<script>
import { mapActions,mapState,mapMutations } from 'vuex';

export default {
    data() {
        return {
        }
    },
    computed: {
        // ...mapState({
        //         count: state => state.count
        //     }),
        ...mapState([
            'count'
        ]),
    },
    methods: {
      
        tincrement() {
            this.aincrement();
        },
        tdecrement() {
            this.$store.commit('decrement');
        },
        nincrement() {
            this.mincrement();
        },
        ...mapMutations({
            mincrement: 'increment',
            mdecrement: 'decrement'
        }),
        ...mapActions([
            'aincrement',
            'adecrement'
        ])
    },
}
</script>