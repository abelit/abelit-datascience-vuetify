<template>
    <div>
        <h1>VuePropDemo 父组件</h1>
        <vue-prop-demo-a pname="yanghui"></vue-prop-demo-a>
    </div>
</template>


<script>
import VuePropDemoA from "@/components/demo/VuePropDemoA";

export default {
    components: {
        VuePropDemoA
    }
}
</script>