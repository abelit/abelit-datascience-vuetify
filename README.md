# abelit-DataScience

## frontend
Vue在密码框使用“ @keyup.enter="submit" ”绑定“Enter回车键”可以实现敲击回车键进行响应
```javascript
  @keyup.enter="submit"
```

Vue通过@focus和@blur来监听焦点事件
```
 @focus="checkUser"
 @blur="checkUser"
```

Vue Prop属性
props用与接收父组件传递给子组件的值

VuePropDemo为父组件
```javascript
//VuePropDemo.vue
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
```

VuePropDemoA为子组件
```javascript
//VuePropDemoA.vue
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
```
