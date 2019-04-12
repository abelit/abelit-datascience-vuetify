<template>
    <div>
        <h1>Slot父组件</h1>
        <vue-slot-demo-a>
            <div>
              父组件的内容：这里父组件的内容会替换子组件中slot组件默认名为default的内容
            </div>
            <template v-slot:footer>
                <div>
                   父组件内容：这里父组件的内容会替换子组件中slot组件名为name="footer"的内容
                </div>
            </template>
        </vue-slot-demo-a>
    </div>
</template>


<script>
import VueSlotDemoA from "@/components/demo/VueSlotDemoA";

export default {
    components: {
        VueSlotDemoA
    }
}
</script>