<template>
    <div id="test">
        <p>
            {{ msg }}
        </p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            msg: "abelit"
        }
    },
    methods: {
        updateName() {
            this.msg = this.msg +" "+ "chenying";
        },
        updateNew() {
            this.updateName();
            this.msg = this.msg + " yeah"
        }
    },
    mounted() {
        this.updateNew();
    },
}
</script>

<style>
    #test {
        padding-top: 80px;
    }
</style>
