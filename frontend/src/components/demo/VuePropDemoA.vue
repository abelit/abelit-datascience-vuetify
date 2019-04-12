<template>
    <div>
        <h1>VuePropDemoA 子组件A</h1>
        <p>{{ pname }}</p>
    </div>
</template>


<script>
export default {
    data () {
        return {}
    },
    props: ["pname"]
}
</script>